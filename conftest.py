import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope='module')
# def main_page(driver):
#     page = MainPage(driver)
#     page.open()
#     return page
