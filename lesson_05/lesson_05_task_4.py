from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Открываем Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Переходим на страницу логина
driver.get("http://the-internet.herokuapp.com/login")

time.sleep(1)

# Вводим username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Вводим password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

time.sleep(1)

# Выводим текст зелёной плашки в консоль
success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text.strip())

# Закрываем браузер
driver.quit()
