from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

def test_add_product_to_cart(driver):

    driver.get(BASE_URL)

    products = ProductsPage(driver)
    cart = CartPage(driver)

    products.click_products()

    products.add_blue_top_to_cart()

    products.click_view_cart()

    assert cart.is_cart_displayed()

    assert cart.is_product_in_cart()