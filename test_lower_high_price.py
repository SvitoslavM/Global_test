import time
import allure
from pages.main_page import MainPage


@allure.story('Open lower price')
def test_lower_price(driver):
    page = MainPage(driver)
    page.open()
    with allure.step('Open all product on main page'):
        open_all = page.open_all_for_lover_price()
    with allure.step("Open lower price on right side page"):
        open_low_price = open_all.open_price_low()
    with allure.step("Open lower price product on page"):
        open_sticker_img = open_all.open_sticker()
    with allure.step('Test lower price product (0.00) is correct'):
        assert open_all.get_low_price_text().text == "$0.00 USD", "Error in price"


@allure.step('Open high price')
def test_high_price(driver):
    page = MainPage(driver)
    page.open()
    open_all_high = page.open_all_for_high_price()
    open_high_price = open_all_high.open_price_high()
    open_jacket = open_all_high.open_bomber_jacket_page()
    assert open_all_high.get_text_price_jacket().text == "$645.99 USD", "Error not correct price"
