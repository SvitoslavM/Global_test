from pages.acme_page_locators import AcmePageLocators
from pages.base_page import BasePage


class AcmePage(BasePage):
    URL = "https://demo.vercel.store/product/acme-cup"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def get_text_acme_cup(self):
        return self.find_element(AcmePageLocators.CHECK_TEXT_ACME_LOCATOR)

    def get_text_acme_cup_card(self):
        return self.find_element(AcmePageLocators.CHECK_ADD_TO_CARD)

    def get_total_price_acme(self):
        return self.find_element(AcmePageLocators.CHECK_TOTAL_PRICE_ACME_CUP_LOCATOR)

    def add_to_basket_acme(self):
        ad_to_basket_acme = self.find_element(AcmePageLocators.ADD_TO_BASKET_ACME)
        ad_to_basket_acme.click()
        return AcmePage(self.driver)

    def add_to_card_acme(self):
        add_to_card = self.find_element(AcmePageLocators.ADD_TO_CARD_ACME)
        add_to_card.click()
        return AcmePage(self.driver)

    def change_total_amount(self):
        change_total = self.find_element(AcmePageLocators.CARD_TOTAL_CHANGE_LOCATOR)
        change_total.click()
        change_total.click()
        change_total.click()
        

        return AcmePage(self.driver)
