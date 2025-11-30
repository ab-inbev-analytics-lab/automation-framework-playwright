import pytest
import os
from utils.logger import get_logger
from utils.azure_devops import create_test_run, get_test_results, update_test_result, close_test_run
from utils.config_reader import config

logger = get_logger(__name__)

# Global run_id for the session
run_id = None

# ---------------------------
# Pytest Hooks
# ---------------------------

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Before all tests: start ADO test run."""
    global run_id,results_data
    try:
        run_id = create_test_run()
        logger.info(f"Created Azure DevOps test run: {run_id}")
        results_data = get_test_results(run_id)
        logger.info(f"Fetched existing test results for run {run_id}")
    except Exception as e:
        logger.error(f"Failed to start Azure DevOps test run: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test result after each phase (setup/call/teardown).
    Stores the report object on the test item for later use.
    """
    outcome = yield
    rep = outcome.get_result()

    # Attach the report to the item so fixtures can access it
    setattr(item, f"rep_{rep.when}", rep)

    # Only publish results after the actual test call
    if rep.when == "call" and run_id:
        marker = item.get_closest_marker("azure_test_case_id")
        if marker:
            test_case_id = marker.args[0]
            duration_ms = int(rep.duration * 1000)
            outcome_str = "Passed" if rep.passed else "Failed"

            matching_result = next(
                (r for r in results_data if r.get("testCase", {}).get("id") == str(test_case_id)),
                None)

            if not matching_result:
                logger.error(f"No existing result found for test case ID {test_case_id} in run {run_id}")
                return

            test_result_id = matching_result["id"]
            logger.info(f"Found matching testResultId: {test_result_id} for testCaseId: {test_case_id}")

            try:
                update_test_result( test_case_id=test_case_id, test_result_id= test_result_id, outcome= outcome_str, duration_ms= duration_ms, run_id= run_id)
                logger.info(f"Sent result for TC{test_case_id} -> {outcome_str}")
            except Exception as e:
                logger.error(f"Failed to send result for TC{test_case_id}: {e}")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """After all tests: close ADO test run."""
    global run_id
    if run_id:
        try:
            close_test_run(run_id)
            logger.info(f"Closed Azure DevOps run {run_id}")
        except Exception as e:
            logger.error(f"Failed to close Azure DevOps run {run_id}: {e}")


# ---------------------------
# Fixtures
# ---------------------------

@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    """
    Launch a Playwright browser for each test.
    Captures a screenshot if the test fails.
    """
    browser_type = config["browser"]
    headless = config["headless"]

    logger.info(f"Launching {browser_type} browser (headless={headless})")
    browser = getattr(playwright_instance, browser_type).launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()

    yield page

    # Screenshot on failure
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        screenshot_dir = os.path.join("screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        page.screenshot(path=screenshot_path)
        logger.error(f"Screenshot saved to {screenshot_path}")

    context.close()
    browser.close()


@pytest.fixture(scope="session")
def playwright_instance():
    """Start Playwright once per test session."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param