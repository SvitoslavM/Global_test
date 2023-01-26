from pages.base_page import BasePage
from pages.price_high_locators import PriceHighLocators


class PriceHighPage(BasePage):
    URL = "https://demo.vercel.store/search"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_price_high(self):
        open_price_high = self.find_element(PriceHighLocators.PRICE_HIGH_LOCATOR)
        open_price_high.click()
        return self.driver

    def open_bomber_jacket_page(self):
        open_jacket = self.find_element(PriceHighLocators.BOMBER_JACKET_LOCATOR)
        open_jacket.click()
        return self.driver

    def get_text_price_jacket(self):
        return self.find_element(PriceHighLocators.BOMBER_JACET_PRICE_LOCATOR)
