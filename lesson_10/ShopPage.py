from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ShopPage:
    def __init__(self, driver):
        """
        Инициализирует страницу интернет-магазина.

        :param driver: WebDriver для управления браузером
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return: None
        """
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)
        self._driver.get('https://www.saucedemo.com/')

    def authorization_username(self, term):
        """
        Вводит имя пользователя в поле авторизации.

        :param term: имя пользователя
        :type term: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#user-name'
        ).send_keys(term)

    def authorization_password(self, term):
        """
        Вводит пароль и нажимает кнопку входа.

        :param term: пароль пользователя
        :type term: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#password'
        ).send_keys(term)
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#login-button'
        ).click()

    def add_to_cart(self):
        """
        Добавляет товары в корзину.

        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#add-to-cart-sauce-labs-backpack'
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#add-to-cart-sauce-labs-bolt-t-shirt'
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#add-to-cart-sauce-labs-onesie'
        ).click()

    def shopping_cart(self):
        """
        Переходит в корзину покупок.

        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            'a.shopping_cart_link'
        ).click()

    def checkout(self):
        """
        Переходит к оформлению заказа.

        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#checkout'
        ).click()

    def input_first_name(self, term):
        """
        Вводит имя покупателя.

        :param term: имя
        :type term: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#first-name'
        ).send_keys(term)

    def input_last_name(self, term):
        """
        Вводит фамилию покупателя.

        :param term: фамилия
        :type term: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#last-name'
        ).send_keys(term)

    def input_postal_code(self, term):
        """
        Вводит почтовый индекс.

        :param term: почтовый индекс
        :type term: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#postal-code'
        ).send_keys(term)

    def button_continue(self):
        """
        Нажимает кнопку продолжения оформления заказа.

        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR,
            '#continue'
        ).click()

    def summary_total(self):
        """
        Получает итоговую сумму заказа.

        :return: строка с итоговой суммой
        :rtype: str
        """
        return self._driver.find_element(
            By.CSS_SELECTOR,
            'div.summary_total_label'
        ).text
