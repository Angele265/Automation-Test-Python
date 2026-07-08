
from pages.login_page import LoginPage


def test_login_user():

    driver.get("https://automationexercise.com")

    login_page = LoginPage(driver)

    login_page.click_signup_login()

    login_page.enter_email("test1751964200@gmail.com")
    login_page.enter_password("TEST_USER_PASSWORD")

    login_page.click_login()

    assert login_page.verify_logged_in()

    login_page.close()