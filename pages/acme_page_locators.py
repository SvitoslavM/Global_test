from selenium.webdriver.common.by import By


class AcmePageLocators:
    CHECK_TEXT_ACME_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/h3/span')
    ADD_TO_BASKET_ACME = (By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/h3/span')
    ADD_TO_CARD_ACME = (By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div[4]/button')
    CHECK_ADD_TO_CARD = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/section/div/div/div/div/div[1]/a/h2')
    CARD_TOTAL_CHANGE_LOCATOR = (
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/section/div/div/div/div/div[1]/ul/li/div[2]/button[3]')
    CHECK_TOTAL_PRICE_ACME_CUP_LOCATOR = (
        By.XPATH, '//*[@id="__next"]/div/div[2]/div/section/div/div/div/div/div[2]/div[1]/span[2]')
