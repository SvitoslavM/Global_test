from selenium.webdriver.common.by import By


class MainPageLocators:
    NEW_ARRIVALS_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[1]/div[1]/nav/a[2]')
    FUTURED_PAGE_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[1]/div[1]/nav/a[3]')
    ALL_PAGE_LOCATOR = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[1]/div[1]/nav/a[1]')
