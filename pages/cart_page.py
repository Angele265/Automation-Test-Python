from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    cart_title = (
        By.XPATH,
        "//li[contains(text(),'Shopping Cart')]"
    )

    blue_top = (
        By.XPATH,
        "//a[text()='Blue Top']"
    )

    def is_cart_displayed(self):
        return "Shopping Cart" in self.driver.page_source

    def is_product_in_cart(self):
        return self.driver.find_element(
            *self.blue_top
        ).is_displayed()

    def remove_product(self):
        self.click(self.remove_product_button)

    def is_product_removed(self):
        return "Blue Top" not in self.driver.page_source