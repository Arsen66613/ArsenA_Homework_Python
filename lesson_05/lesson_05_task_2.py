from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Запускаем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

time.sleep(2)

# строгий XPath для класса btn-primary
xpath = (
    "//button[contains(concat(' ', normalize-space(@class), ' '), "
    "' btn-primary ')]"
)

# Находим кнопку
button = driver.find_element(By.XPATH, xpath)

# Кликаем
button.click()

time.sleep(2)

# Закрываем браузер
driver.quit()
