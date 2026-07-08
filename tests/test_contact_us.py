import os

from pages.contact_page import ContactPage
from utils.config import BASE_URL
from data.test_data import (
    CONTACT_NAME,
    CONTACT_EMAIL,
    CONTACT_SUBJECT,
    CONTACT_MESSAGE
)



def test_contact_us_form(driver):

    driver.get(BASE_URL)

    contact = ContactPage(driver)

    contact.click_contact_us()

    contact.enter_name(CONTACT_NAME)
    contact.enter_email(CONTACT_EMAIL)
    contact.enter_subject(CONTACT_SUBJECT)
    contact.enter_message(CONTACT_MESSAGE)

    file_path = os.path.abspath(
        "test_files/test_file.txt"
    )

    contact.upload_file(file_path)

    contact.submit()

    alert = driver.switch_to.alert
    alert.accept()

    assert contact.verify_success_message()