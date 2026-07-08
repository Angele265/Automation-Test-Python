from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    product_name = (
        By.XPATH,
        "//div[@class='product-information']/h2"
    )

    product_price = (
        By.XPATH,
        "//div[@class='product-information']/span/span"
    )

    availability = (
        By.XPATH,
        "//div[@class='product-information']//p[contains(text(),'Availability')]"
    )

    condition = (
        By.XPATH,
        "//div[@class='product-information']//p[contains(text(),'Condition')]"
    )

    brand = (
        By.XPATH,
        "//div[@class='product-information']//p[contains(text(),'Brand')]"
    )


    def get_product_name(self):
        return self.get_text(self.product_name)


    def get_product_price(self):
        return self.get_text(self.product_price)


    def get_availability(self):
        return self.get_text(self.availability)


    def get_condition(self):
        return self.get_text(self.condition)


    def get_brand(self):
        return self.get_text(self.brand)