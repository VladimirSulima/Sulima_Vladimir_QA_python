from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class ResellerPortalLoginPage:
    def __init__(self, driver):
        self.driver = driver

    # region Set actions

    def set_login_name(self, login):
        self.driver.wait.until(ec.visibility_of_element_located((By.ID, "resellerUsername")))
        self.driver.instance.find_element_by_id("resellerUsername").send_keys(login)

        return self

    def set_password(self, password):
        self.driver.instance.find_element_by_id("resellerPassword").send_keys(password)

        return self
    # endregion

    # region Click actions
    def click_sign_in_button(self):
        self.driver.instance.find_element_by_xpath("//button[@ng-click='login.getUserLogin()']").click()

        return self
    # endregion

    # region Get actions
    def get_error_message(self):
        error_message = self.driver.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "error")))

        return error_message.text
    # endregion

    # region Check actions
    def check_error_message(self, expected_message, actual_message):
        assert expected_message in actual_message, f"Error message at Reseller Portal Login page not as expected."
    # endregion
