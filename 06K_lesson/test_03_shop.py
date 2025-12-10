from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_of_element_located(css, driver):
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, css)
        )
    )
    return element


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

username = wait_of_element_located(css='#user-name', driver=driver)
password = wait_of_element_located(css='#password', driver=driver)

username.send_keys('standard_user')
password.send_keys('secret_sauce')


wait_of_element_located(
    css='#login-button', driver=driver
    ).click()
wait_of_element_located(
    css='#add-to-cart-sauce-labs-backpack', driver=driver
    ).click()
wait_of_element_located(
    css='#add-to-cart-sauce-labs-bolt-t-shirt', driver=driver
    ).click()
wait_of_element_located(
    css='#add-to-cart-sauce-labs-onesie', driver=driver
    ).click()
wait_of_element_located(
    css='a.shopping_cart_link', driver=driver
    ).click()
wait_of_element_located(css='#checkout', driver=driver).click()

first_name = wait_of_element_located(css='#first-name', driver=driver)
last_name = wait_of_element_located(css='#last-name', driver=driver)
postal_code = wait_of_element_located(css='#postal-code', driver=driver)

first_name.send_keys('Arsen')
last_name.send_keys('Avakian')
postal_code.send_keys('00000')

wait_of_element_located(css='#continue', driver=driver).click()


def test_total():
    total = wait_of_element_located(
        css='div.summary_total_label', driver=driver
        )
    assert total.text == 'Total: $58.29'

    driver.quit()
