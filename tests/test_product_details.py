from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from data.test_data import EXPECTED_PRODUCT_NAME
from utils.config import BASE_URL


def test_verify_product_details(driver):

    driver.get(BASE_URL)

    products = ProductsPage(driver)
    details = ProductDetailsPage(driver)

    products.click_products()

    products.click_view_product()

    assert details.get_product_name() == EXPECTED_PRODUCT_NAME

    assert details.get_availability() != ""

    assert details.get_condition() != ""

    assert details.get_brand() != ""