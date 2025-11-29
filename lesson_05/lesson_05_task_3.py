from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Открываем браузер Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Переходим на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

time.sleep(1)

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим Sky
input_field.send_keys("Sky")
time.sleep(1)

# Очищаем поле
input_field.clear()
time.sleep(1)

# Вводим Pro
input_field.send_keys("Pro")
time.sleep(1)

# Закрываем браузер
driver.quit()
