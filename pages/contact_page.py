from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactPage(BasePage):

    contact_us = (
        By.XPATH,
        "//a[contains(text(),'Contact us')]"
    )

    name_field = (
        By.NAME,
        "name"
    )

    email_field = (
        By.NAME,
        "email"
    )

    subject_field = (
        By.NAME,
        "subject"
    )

    message_field = (
        By.ID,
        "message"
    )

    upload_file = (
        By.NAME,
        "upload_file"
    )

    submit_button = (
        By.NAME,
        "submit"
    )

    success_message = (
        By.XPATH,
        "//div[contains(text(),'Success! Your details have been submitted successfully.')]"
    )


    def click_contact_us(self):
        self.click(self.contact_us)


    def enter_name(self, name):
        self.type_text(self.name_field, name)


    def enter_email(self, email):
        self.type_text(self.email_field, email)


    def enter_subject(self, subject):
        self.type_text(self.subject_field, subject)


    def enter_message(self, message):
        self.type_text(self.message_field, message)


    def upload_file(self, file_path):
        self.driver.find_element(
            *self.upload_file
        ).send_keys(file_path)


    def submit_form(self):
        self.click(self.submit_button)


    def verify_success_message(self):
        return self.driver.find_element(
            *self.success_message
        ).is_displayed()