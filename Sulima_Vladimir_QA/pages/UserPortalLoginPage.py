from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.ResellerPortalLoginPage import ResellerPortalLoginPage


class UserPortalLoginPage:

    def __init__(self, driver):
        self.driver = driver

    # region Set actions
    def set_login_name(self, login):
        self.driver.instance.find_element_by_id("username").send_keys(login)
        return self

    def set_password(self, password):
        self.driver.instance.find_element_by_id("password").send_keys(password)
        return self
    # endregion

    # region Click actions
    def click_sign_in_button(self):
        self.driver.instance.find_element_by_xpath("//button[@ng-click='login(username, password)']").click()
        return self

    def click_reseller_portal_button(self):
        self.driver.instance.find_element_by_xpath("//a[text()='Reseller Portal']").click()
        return ResellerPortalLoginPage(self.driver)
    # endregion

    # region Get actions
    def get_warning_message(self):
        warning_message = self.driver.wait.until(ec.visibility_of_element_located
                                          ((By.XPATH, "//div[@ng-show='error']/span[@class='warning']")))
        return warning_message.text
    # endregion

    # region Check actions
    def check_warning_message(self, expected_message, actual_message):
        assert expected_message == actual_message, f"Warning message at User Portal Login page not as expected. " \
                                                   f"Was '{actual_message}' but should be '{expected_message}'"
    # endregion

