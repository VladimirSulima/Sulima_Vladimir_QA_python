import unittest

from scenarios.LoginScenarios import UserLogin
from scenarios.NavigationScenarios import NavigationScenarios
from webdriver import Driver
from values import strings


class LoginVerification(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.instance.maximize_window()
        self.driver.navigate(strings.base_url)

    def test_user_login_with_invalid_credentials(self):
        page = UserLogin(self.driver)

        page.login_to_user_portal("some@login.com", "password")\
            .verify_warning_message(expected_message="The user or password is incorrect.")

    def test_reseller_login_with_invalid_credentials(self):
        page = NavigationScenarios(self.driver)

        page.navigate_to_reseller_portal_page()\
            .login_to_reseller_portal("some@login.com", "password")\
            .verify_error_message(expected_message="401 Client Error:")

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()

