from playwright.sync_api import Page
from base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Navigation Bar Locators
        self.challenges = "ul[class*='flex-col'] a[href='#challenges']"
        self.howItWorks = "ul[class*='flex-col'] a[href='#how-it-works']"
        self.features = "ul[class*='flex-col'] a[href='#features']"
        self.kpiFramework = "ul[class*='flex-col'] a[href='#kpi-framework']"
        self.whyBrewMetrics = "ul[class*='flex-col'] a[href='#why-brew-metrics']"
        self.contact = "ul[class*='flex-col'] a[href='#contact']"
        self.languageSelector = "header div[class*='lg:flex'] div[class='relative']"
        self.lightMode="div[class*='justify-between'] div[class*='flex shadow'] a:nth-of-type(1)"
        self.darkMode="div[class*='justify-between'] div[class*='flex shadow'] a:nth-of-type(2)"

    def navigate(self):
        """Navigate to the Sauce Demo login page."""
        self.page.goto("<brew_metrics_link>")