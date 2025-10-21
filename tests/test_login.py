from pages.login_page import LoginPage
from utils.config_reader import config
from utils.logger import get_logger
import pytest

logger = get_logger(__name__)

@pytest.mark.azure_test_case_id(128285)
def test_login(browser):
    logger.info("Starting login test")
    login_page = LoginPage(browser)
    login_page.navigate(config["base_url"])
    login_page.login(config["username"], config["password"])
    assert "Swag Labs" in login_page.get_title()

@pytest.mark.azure_test_case_id(128702)
def test_login_error(browser):
    logger.info("Starting login test to verify if ther error message is displayed")
    login_page = LoginPage(browser)
    login_page.navigate(config["base_url"])
    login_page.login(config["username"], "password")
    login_page.verify_error_message()