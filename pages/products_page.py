from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    products_button = (
        By.XPATH,
        "//a[contains(text(),'Products')]"
    )

    search_box = (
        By.ID,
        "search_product"
    )

    search_button = (
        By.ID,
        "submit_search"
    )

    searched_products_title = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )

    blue_top_product = (
        By.XPATH,
        "//p[text()='Blue Top']"
    )

    add_blue_top = (
        By.XPATH,
        "//a[@data-product-id='1']"
    )

    view_cart = (
        By.XPATH,
        "//u[text()='View Cart']"
    )

    view_product = (
        By.XPATH,
        "//a[contains(text(),'View Product')]"
    )

    def click_products(self):
        self.click(self.products_button)

    def search_product(self, product_name):
        self.type_text(self.search_box, product_name)

    def click_search(self):
        self.click(self.search_button)

    def is_search_results_displayed(self):
        return self.get_text(
            self.searched_products_title
        ) == "SEARCHED PRODUCTS"

    def is_blue_top_displayed(self):
        return self.driver.find_element(
            *self.blue_top_product
        ).is_displayed()

    def add_blue_top_to_cart(self):
        self.click(self.add_blue_top)

    def click_view_cart(self):
        self.click(self.view_cart)

    def click_view_product(self):
        self.click(self.view_product)