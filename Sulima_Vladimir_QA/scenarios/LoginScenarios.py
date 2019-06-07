from pages.ResellerPortalLoginPage import ResellerPortalLoginPage
from pages.UserPortalLoginPage import UserPortalLoginPage


class UserLogin:
    def __init__(self, driver):
        self.driver = driver

    def login_to_user_portal(self, login_name, password):
        login_page = UserPortalLoginPage(self.driver)

        login_page\
            .set_login_name(login_name)\
            .set_password(password).\
            click_sign_in_button()

        return self

    def verify_warning_message(self, expected_message):
        page = UserPortalLoginPage(self.driver)

        actual_warning_message = page.get_warning_message()
        page.check_warning_message(expected_message=expected_message,
                                   actual_message=actual_warning_message)

        return self


class ResellerLogin():
    def __init__(self, driver):
        self.driver = driver

    def login_to_reseller_portal(self, login, password):
        page = ResellerPortalLoginPage(self.driver)

        page.set_login_name(login) \
            .set_password(password) \
            .click_sign_in_button()

        return self

    def verify_error_message(self, expected_message):
        page = ResellerPortalLoginPage(self.driver)

        actual_error_message = page.get_error_message()
        page.check_error_message(expected_message=expected_message,
                                 actual_message=actual_error_message)
        return self
