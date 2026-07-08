from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    email_field = (By.XPATH, "//input[@data-qa='login-email']")
    password_field = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    logged_in_user = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def enter_email(self, email):
        self.type_text(self.email_field, email)

    def enter_password(self, password):
        self.type_text(self.password_field, password)

    def click_login(self):
        self.click(self.login_button)

    def verify_logged_in(self):
        return self.driver.find_element(
            *self.logged_in_user
        ).is_displayed()