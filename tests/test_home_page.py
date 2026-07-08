from utils.driver_factory import DriverFactory
from pages.home_page import HomePage



def test_home_page_title():
    driver = DriverFactory.get_driver()

    home_page = HomePage(driver)

    home_page.open()

    assert home_page.get_title() == "Automation Exercise"

    home_page.close()
