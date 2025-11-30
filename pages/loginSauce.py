from playwright.sync_api import Page

class LoginSaucePage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        """Navigate to the Sauce Demo login page."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """Fill in credentials and log in."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)