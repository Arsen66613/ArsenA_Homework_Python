from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from ShopPage import ShopPage


def test_shop_buy():
    browser = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
        )

    buy = ShopPage(browser)
    buy.authorization_username('standard_user')
    buy.authorization_password('secret_sauce')
    buy.add_to_cart()
    buy.shopping_cart()
    buy.checkout()
    buy.input_first_name('Arsen')
    buy.input_last_name('Avakian')
    buy.input_postal_code('00000')
    buy.button_continue()
    total = buy.summary_total()

    assert total == 'Total: $58.29'

    browser.quit()
