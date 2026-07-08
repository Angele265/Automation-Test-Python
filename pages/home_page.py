from pages.base_page import BasePage
from utils.config import BASE_URL


class HomePage(BasePage):

    def open(self):
        self.driver.get(BASE_URL)

    def click_signup_login(self):
        self.click(self.signup_login_button)