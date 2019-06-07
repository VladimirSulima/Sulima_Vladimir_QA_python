from pages.UserPortalLoginPage import UserPortalLoginPage
from scenarios.LoginScenarios import ResellerLogin


class NavigationScenarios:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_reseller_portal_page(self):
        page = UserPortalLoginPage(self.driver)
        page.click_reseller_portal_button()

        return ResellerLogin(self.driver)
