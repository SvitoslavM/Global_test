import time
import allure
from pages.main_page import MainPage


@allure.story('open_futured')
def test_futured_page(driver):
    page = MainPage(driver)
    page.open()
    with allure.step('Open futured page'):
        open_future_page = page.open_futured_page()
    with allure.step('Open ACME Cup page'):
        open_acme = open_future_page.open_acme_cup()
    with allure.step('Test text on page "ACME Cup"'):
        assert open_acme.get_text_acme_cup().text == "ACME Cup", "Wrong name, Error"


@allure.story('Add to card ACME Cup')
def test_add_to_basket_acme(driver):
    page = MainPage(driver)
    page.open()
    with allure.step('open futured_page'):
        open_future_page = page.open_futured_page()
    with allure.step('Open ACME Cup page'):
        open_acme = open_future_page.open_acme_cup()
    with allure.step('Click on "add to card" Acme cup'):
        card_acme = open_acme.add_to_card_acme()
    with allure.step('Test text after click "Add to card" text == "My Cart"'):
        assert card_acme.get_text_acme_cup_card().text == 'My Cart', "DIDN'T ADD TO CARD CUP"


@allure.story('Check total price after add to card and change amount on * 5')
def test_change_total_cup(driver):
    page = MainPage(driver)
    page.open()
    open_future_page = page.open_futured_page()
    open_acme = open_future_page.open_acme_cup()
    get_total = open_acme.add_to_card_acme().change_total_amount()
    """Used sleep because not work with time waiter's"""
    time.sleep(2)
    with allure.step('Test text after change amount *5 == 125$'):
        assert get_total.get_total_price_acme().text == '$125.00', "ERROR WRONG PRICE"

