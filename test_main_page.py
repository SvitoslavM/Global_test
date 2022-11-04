from pages.main_page import MainPage


def test_futured_page(driver):
    page = MainPage(driver)
    page.open()
    futured_page = page.open_futured_page()
    acme_page = futured_page.open_acme_cup()
    assert acme_page.get_text_acme_cup().text == "ACME Cup", "error"
