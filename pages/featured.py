from pages.acme_page import AcmePage
from pages.base_page import BasePage
from pages.featured_page_locators import FuturedPageLocators


class FuturedPage(BasePage):
    URL = "https://demo.vercel.store/search/featured"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def get_text_futured(self):
        return self.find_element(FuturedPageLocators.CHECK_TEXT_FUTERED_LOCATOR)

    def open_acme_cup(self):
        open_acme = self.find_element(FuturedPageLocators.ACME_CUP_LOCATOR)
        open_acme.click()
        return AcmePage(self.driver)
