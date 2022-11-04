from pages.base_page import BasePage
from pages.featured import FuturedPage
from pages.main_page_locators import MainPageLocators


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