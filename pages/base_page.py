from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def get_title(self):
        title = self.page.title()
        logger.info(f"Page title: {title}")
        return title

    def take_screenshot(self, path):
        self.page.screenshot(path=path)
    
    def click_by_text(self, text):
        self.page.get_by_text(text, exact=True).click()

    def validate_text(self, selector, expected_text):
        actual_text = self.page.locator(selector).text_content()
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
