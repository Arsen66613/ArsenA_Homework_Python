from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CalculatorPage():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self._driver.implicitly_wait(47)

    def delay(self, term):
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    def click(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]'
        ).click()  # Кнопка "7"
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]'
        ).click()  # Кнопка "+"
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]'
        ).click()  # Кнопка "8"
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]'
        ).click()  # Кнопка "="

    def screen(self):
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 47).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15")
        )
        return screen.text
