from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from data.test_data import (
    TEST_EMAIL,
    TEST_PASSWORD,
    CARD_NAME,
    CARD_NUMBER,
    CARD_CVC,
    CARD_MONTH,
    CARD_YEAR
)


def test_place_order(driver):

    driver.get(
        "https://automationexercise.com"
    )

    home = HomePage(driver)
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)


    # Login
    home.click_signup_login()

    login.enter_email(TEST_EMAIL)
    login.enter_password(TEST_PASSWORD)
    login.click_login()

    assert login.is_user_logged_in()


    # Add product
    products.click_products()

    products.add_blue_top_to_cart()

    products.click_view_cart()


    # Checkout
    checkout.click_proceed_checkout()

    checkout.click_place_order()


    # Payment
    checkout.enter_payment_details(
        CARD_NAME,
        CARD_NUMBER,
        CARD_CVC,
        CARD_MONTH,
        CARD_YEAR
    )

    checkout.click_pay()


    # Verify order
    assert (
        "Congratulations!"
        in checkout.is_order_confirmed()
    )