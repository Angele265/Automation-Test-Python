from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    proceed_checkout = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    name_on_card = (
        By.NAME,
        "name_on_card"
    )

    card_number = (
        By.NAME,
        "card_number"
    )

    cvc = (
        By.NAME,
        "cvc"
    )

    expiry_month = (
        By.NAME,
        "expiry_month"
    )

    expiry_year = (
        By.NAME,
        "expiry_year"
    )

    pay_button = (
        By.ID,
        "submit"
    )

    order_success = (
        By.XPATH,
        "//p[contains(text(),'Congratulations! Your order has been confirmed!')]"
    )


    def click_checkout(self):
        self.click(self.proceed_checkout)


    def enter_payment_details(
        self,
        name,
        card,
        cvc,
        month,
        year
    ):
        self.type_text(self.name_on_card, name)
        self.type_text(self.card_number, card)
        self.type_text(self.cvc, cvc)
        self.type_text(self.expiry_month, month)
        self.type_text(self.expiry_year, year)


    def pay_order(self):
        self.click(self.pay_button)


    def verify_order_success(self):
        return self.get_text(
            self.order_success
        )