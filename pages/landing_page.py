from playwright.sync_api import Page
from base_page import BasePage
from playwright.sync_api import expect

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        #Navigation Bar Locators
        self.challenges = "ul[class*='flex-col'] a[href='#challenges']"
        self.howItWorks = "ul[class*='flex-col'] a[href='#how-it-works']"
        self.features = "ul[class*='flex-col'] a[href='#features']"
        self.kpiFramework = "ul[class*='flex-col'] a[href='#kpi-framework']"
        self.whyBrewMetrics = "ul[class*='flex-col'] a[href='#why-brew-metrics']"
        self.contact = "ul[class*='flex-col'] a[href='#contact']"
        self.languageSelector = "header div[class*='lg:flex'] div[class='relative']"
        self.lightMode="div[class*='justify-between'] div[class*='flex shadow'] a:nth-of-type(1)"
        self.darkMode="div[class*='justify-between'] div[class*='flex shadow'] a:nth-of-type(2)"
        self.currChalengSolution="section[id='challenges'] div[class*='card']"

    def navigate(self,url):
        super().navigate(url)

    def clickOnChallenges(self):
        self.page.click(self.challenges)
    
    def clickOnHowItWorks(self):
        self.page.click(self.howItWorks)

    def clickOnFeatures(self):
        self.page.click(self.features)

    def clickOnKPIFramework(self):
        self.page.click(self.kpiFramework)

    def clickOnWhyBrewMetrics(self):
        self.page.click(self.whyBrewMetrics)

    def clickOnContact(self):
        self.page.click(self.contact)

    def clickOnLangSelector(self):
        self.page.click(self.languageSelector)
    
    def selectLightMode(self):
        self.page.click(self.lightMode)

    def selectDarkMode(self):
        self.page.click(self.darkMode)

    def clickToViewHeatMap(self):
        expect(self.page.get_by_text("Check the Challenges in Heatmap")).to_be_visible()
        super().click_by_text(self, "Check the Challenges in Heatmap")


