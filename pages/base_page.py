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
