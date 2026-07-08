from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD


def test_logout_user(driver):

    driver.get("https://automationexercise.com")

    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.click_signup_login()

    login_page.enter_email(TEST_USER_EMAIL)
    login_page.enter_password(TEST_USER_PASSWORD)
    login_page.click_login()

    assert login_page.is_user_logged_in()

    login_page.click_logout()

    assert login_page.is_login_page_displayed()