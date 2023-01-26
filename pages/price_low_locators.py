from selenium.webdriver.common.by import By


class PriceLowLocators:
    CHANGE_PRICE_LOW_TO_HIGHT_LOCATOR = (
        By.XPATH, '//*[@id="__next"]/div/main/div/div/div[3]/div/div[2]/div/div/ul/li[4]/a')
    CHOOSE_LOWER_PRICE_STICKER_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/main/div/div/div[2]/div/a[1]/div[2]/img')
    CHOOSE_PRICE_STICKER_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div[1]/div')
