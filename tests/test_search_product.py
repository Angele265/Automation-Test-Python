from pages.products_page import ProductsPage
from data.test_data import SEARCH_PRODUCT


def test_search_product(driver):

    driver.get("https://automationexercise.com")

    products = ProductsPage(driver)

    products.click_products()

    products.search_product(SEARCH_PRODUCT)

    products.click_search()

    assert products.is_search_results_displayed()

    assert products.is_blue_top_displayed()