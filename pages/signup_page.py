from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):

    # Locators
    signup_login_button = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    name_field = (By.NAME, "name")
    email_field = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")

    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_button).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    account_created_message = (
        By.XPATH,
        "//h2[contains(text(),'Account Created')]"
    )

    continue_button = (
        By.XPATH,
        "//a[@data-qa='continue-button']"
    )

    def verify_account_created(self):
        return self.driver.find_element(
            *self.account_created_message
        ).is_displayed()

    def click_continue(self):
        self.click(self.continue_button)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()