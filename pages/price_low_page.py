from pages.price_low_locators import PriceLowLocators
from pages.base_page import BasePage


class PriceLowPage(BasePage):
    URL = "https://demo.vercel.store/search"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_price_low(self):
        open_price_low = self.find_element(PriceLowLocators.CHANGE_PRICE_LOW_TO_HIGHT_LOCATOR)
        open_price_low.click()

    def open_sticker(self):
        open_sticker = self.find_element(PriceLowLocators.CHOOSE_LOWER_PRICE_STICKER_LOCATOR)
        open_sticker.click()
        return self.driver

    def get_low_price_text(self):
        return self.find_element(PriceLowLocators.CHOOSE_PRICE_STICKER_LOCATOR)
