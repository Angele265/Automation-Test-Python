
from pages.login_page import LoginPage
from data.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.config import BASE_URL

def test_login_user():

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.click_signup_login()

    login_page.enter_email(TEST_USER_EMAIL)
    login_page.enter_password(TEST_USER_PASSWORD)

    login_page.click_login()

    assert login_page.verify_logged_in()

    login_page.close()