import requests
from datetime import datetime , UTC
from utils.config_reader import config
from utils.logger import get_logger

logger = get_logger(__name__)

def _get_auth():
    """Return HTTP Basic Auth for Azure DevOps using PAT."""
    pat_token = config["azure_devops"]["pat_token"]
    return requests.auth.HTTPBasicAuth("", pat_token)

def _get_base_info():
    """Return common ADO config values."""
    return (
        config["azure_devops"]["organization"],
        config["azure_devops"]["project"],
        config["azure_devops"]["test_plan_id"],
        config["azure_devops"]["test_suite_id"]
    )

def create_test_run():
    """
    Create a new test run in Azure DevOps Test Plans.
    Returns the run_id.
    """
    org, project, plan_id, suite_id = _get_base_info()
    url = f"https://dev.azure.com/{org}/{project}/_apis/test/runs?api-version=7.0"

    payload = {
        "name": f"Pytest Run - {datetime.now(UTC).isoformat()}",
        "plan": {"id": plan_id},
        "automated": True,
        "state": "InProgress",
        "startDate": datetime.now(UTC).isoformat(),
        "pointIds": _get_all_point_ids(org, project, plan_id, suite_id)
    }

    logger.info(f"Creating ADO test run for plan {plan_id}...")
    response = requests.post(url, json=payload, auth=_get_auth())

    if response.status_code in [200, 201]:
        run_id = response.json()["id"]
        logger.info(f"Created test run {run_id}")
        return run_id
    else:
        logger.error(f"Failed to create test run: {response.status_code} - {response.text}")
        raise RuntimeError("Failed to create test run")

def get_test_results(run_id):
    org, project, plan_id, suite_id = _get_base_info()
    results_resp = requests.get(
        f"https://dev.azure.com/{org}/{project}/_apis/test/Runs/{run_id}/Results?api-version=7.0", auth=_get_auth()
    )
    results_resp.raise_for_status()
    results_data = results_resp.json().get("value", [])
    return results_data
def _get_all_point_ids(org, project, plan_id, suite_id):
    """Fetch all test point IDs for the given plan/suite."""
    url = f"https://dev.azure.com/{org}/{project}/_apis/testplan/Plans/{plan_id}/Suites/{suite_id}/TestPoint?api-version=7.0"
    response = requests.get(url, auth=_get_auth())
    if response.status_code == 200:
        points = response.json().get("value", [])
        return [p["id"] for p in points]
    else:
        logger.error(f"Failed to fetch test points: {response.status_code} - {response.text}")
        return []

def update_test_result(test_case_id, test_result_id, outcome, duration_ms, run_id, comment=""):
    """
    Update a single test case result in the given run.
    """
    org, project, _, _ = _get_base_info()
    url = f"https://dev.azure.com/{org}/{project}/_apis/test/Runs/{run_id}/Results?api-version=7.0"
    payload = [{
        "id": test_result_id,
        "testCase": {"id": str(test_case_id)},
        "outcome": outcome,  # "Passed" or "Failed"
        "state": "Completed",
        "startedDate": datetime.now(UTC).isoformat(),
        "completedDate": datetime.now(UTC).isoformat(),
        "durationInMs": duration_ms,
        "comment": comment
    }]

    logger.info(f"Payloading test result for TestCase {test_case_id}: {payload}")

    logger.info(f"Updating result for TestCase {test_case_id} -> {outcome}")
    response = requests.patch(url, json=payload, auth=_get_auth())

    if response.status_code in [200, 201, 204]:
        logger.info("Test result updated successfully.")
    else:
        logger.error(f"Failed to update result: {response.status_code} - {response.text}")

def close_test_run(run_id):
    """
    Mark the test run as completed.
    """
    org, project, _, _ = _get_base_info()
    url = f"https://dev.azure.com/{org}/{project}/_apis/test/runs/{run_id}?api-version=7.0"

    payload = {
        "state": "Completed",
        "completedDate": datetime.now(UTC).isoformat()
    }

    logger.info(f"Closing test run {run_id}...")
    response = requests.patch(url, json=payload, auth=_get_auth())

    if response.status_code in [200, 201, 204]:
        logger.info(f"Test run {run_id} closed successfully.")
    else:
        logger.error(f"Failed to close test run: {response.status_code} - {response.text}")
