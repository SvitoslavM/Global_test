import pytest
from selenium import webdriver

# @pytest.fixture(scope='session')
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
