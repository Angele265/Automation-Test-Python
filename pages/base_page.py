from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger()

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self, locator, text):
        self.logger.info(
            f"Entering text '{text}' into element: {locator}"
        )

        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_title(self):
        self.logger.info("Getting page title")
        return self.driver.title

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def close(self):
        self.logger.info("Closing browser")
        self.driver.quit()