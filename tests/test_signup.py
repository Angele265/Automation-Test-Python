import time

from pages.signup_page import SignupPage
from utils.driver_factory import DriverFactory
from data.test_data import TEST_USER_NAME
from utils.data_generator import generate_email



def test_register_new_user():

    driver = DriverFactory.get_driver()

    signup = SignupPage(driver)

    driver.get("https://automationexercise.com")

    signup.click_signup_login()

    email = generate_email()

    signup.enter_name(TEST_USER_NAME)
    signup.enter_email(email)

    signup.click_signup()

    assert signup.verify_account_created()

    driver.quit()