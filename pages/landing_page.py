from playwright.sync_api import Page
from base_page import BasePage
from playwright.sync_api import expect

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
        
        # Current Challenges & Solutions Locators
        self.currChalengSolution="section[id='challenges'] div[class*='card']"
        
        # How BrewMetrics Works Locators
        self.howBrewMetricsWorks="section[id='how-it-works'] h1"
        self.howBrewMetricsWorksContent="section[id='how-it-works'] h1+div"
        
        # Key Features Locators
        self.keyFeatures="section[id='features'] h1"
        self.keyFeaturesContent="section[id='features'] h1+div"
        self.smartGovernanceImage="section[id='features'] img[src*='smart_governance_bg.png']"
        self.smartGovernanceTitle="section[id='features'] div[class='mt-8'] div[class*='mt-6'] h2"
        self.smartGovernanceDescription="section[id='features'] div[class='mt-8'] div[class*='mt-6'] p"
        self.smartGovernanceLink="section[id='features'] div[class='mt-8'] div[class*='mt-6'] a"

        # KPI Framework Locators
        self.kpiFrameworkSectionTitle="section[id='kpi-framework'] h1>span"
        self.kpiFrameworkStatement="section[id='kpi-framework'] div[class*='text-lg']"
        
        
        

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
        
    def verifyHowBrewMetricsWorksSection(self):
        expect(self.page.locator(self.howBrewMetricsWorks)).to_be_visible()
        expect(self.page.locator(self.howBrewMetricsWorksContent)).to_be_visible()
        super().validate_text(self.howBrewMetricsWorks, "How BrewMetrics Works")
        super().validate_text(self.howBrewMetricsWorksContent, "Extract data from code repositories, Project Management tools etc. Analysis KPI's and fix the gaps in real time")
        
    def verifyKeyFeaturesSection(self):
        expect(self.page.locator(self.keyFeatures)).to_be_visible()
        expect(self.page.locator(self.keyFeaturesContent)).to_be_visible()
        super().validate_text(self.keyFeatures, "Key Features")
        super().validate_text(self.keyFeaturesContent, "Our platform combines real-time data monitoring, AI-powered recommendations, and KPI governance to help teams move faster with confidence")
    
    def verifySmartGovernanceFeature(self):
        expect(self.page.locator(self.smartGovernanceImage)).to_be_visible()
        expect(self.page.locator(self.smartGovernanceTitle)).to_be_visible()
        expect(self.page.locator(self.smartGovernanceDescription)).to_be_visible()
        expect(self.page.locator(self.smartGovernanceLink)).to_be_visible()
        super().validate_text(self.smartGovernanceTitle, "Smart Governance")
        super().validate_text(self.smartGovernanceDescription, "Extract and sanitize datasets from multiple products and tools. Apply custom formulas to define precise KPI values for comprehensive analytics.")
        super().validate_text(self.smartGovernanceLink, "Learn More")
        