from pages.base_page import BasePage
from pages.new_arrivals_page_locators import NewArrivalsLocators


class NewArrivalsPage(BasePage):
    URL = "https://demo.vercel.store/search/clothes"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_new_arrival(self):
        open_acme_cup = self.find_element(NewArrivalsLocators.ACME_CUP_LOCATOR)
        open_acme_cup.click()

