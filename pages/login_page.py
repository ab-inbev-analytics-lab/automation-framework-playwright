from .base_page import BasePage
from utils.config_reader import config
from utils.logger import get_logger

logger = get_logger(__name__)
class LoginPage(BasePage):
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"

    def login(self, username, password):
        logger.info(f"Entering username: {username}")
        self.page.fill(self.username_input, username)
        logger.info("Entering password")
        self.page.fill(self.password_input, password)
        logger.info("Clicking login button")
        self.page.click(self.login_button)
    
    def verify_error_message(self):
        error_selector = "[data-test='error']"
        actual_message = self.page.text_content(error_selector)
        assert actual_message is not None, "No error message displayed"
