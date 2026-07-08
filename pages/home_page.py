from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get("https://automationexercise.com")

    def click_signup_login(self):
        self.click(self.signup_login_button)