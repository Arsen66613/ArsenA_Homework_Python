from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
    waiter = WebDriverWait(driver, 47, poll_frequency=0.1)

    delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys('45')

    # Нажатие кнопок калькулятора
    driver.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[1]'
        ).click()
    driver.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[4]'
        ).click()
    driver.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[2]'
        ).click()
    driver.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[15]'
        ).click()

    # Элемент экрана
    screen = driver.find_element(By.CSS_SELECTOR, 'div.screen')
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    # Проверка результата
    assert screen.text == "15"

    driver.quit()
