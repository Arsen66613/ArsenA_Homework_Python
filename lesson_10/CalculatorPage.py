from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.

        :param driver: WebDriver для управления браузером
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def delay(self, term):
        """
        Устанавливает задержку вычисления.

        :param term: значение задержки в секундах
        :type term: str
        :return: None
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    def click(self):
        """
        Выполняет операцию 7 + 8 = на калькуляторе.

        :return: None
        """
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]'
        ).click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]'
        ).click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]'
        ).click()
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]'
        ).click()

    def screen(self):
        """
        Ожидает результат вычисления и возвращает его.

        :return: результат вычисления
        :rtype: str
        """
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 47).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
            )
        )
        return screen.text
