from pages.base_page import BasePage
from pages.featured import FuturedPage
from pages.main_page_locators import MainPageLocators
from pages.price_high_page import PriceHighPage
from pages.price_low_page import PriceLowPage


class MainPage(BasePage):
    URL = "https://demo.vercel.store/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_new_arrival(self):
        open_arrival = self.find_element(MainPageLocators.NEW_ARRIVALS_LOCATOR)
        open_arrival.click()

    def open_futured_page(self):
        open_futured = self.find_element(MainPageLocators.FUTURED_PAGE_LOCATOR)
        open_futured.click()
        return FuturedPage(self.driver)

    def open_all_for_lover_price(self):
        open_all = self.find_element(MainPageLocators.ALL_PAGE_LOCATOR)
        open_all.click()
        return PriceLowPage(self.driver)

    def open_all_for_high_price(self):
        open_all = self.find_element(MainPageLocators.ALL_PAGE_LOCATOR)
        open_all.click()
        return PriceHighPage(self.driver)