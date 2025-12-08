from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

# Задание 1
driver.implicitly_wait(17)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = driver.find_element(By.CSS_SELECTOR, '#content')
txt = content.find_element(By.CSS_SELECTOR, 'p.bg-success').text
print(txt)

quit()

# Задание 3
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
driver.implicitly_wait(20)

images = driver.find_elements(By.TAG_NAME, "img")

third_img_src = images[2].get_attribute("src")

print(third_img_src)


sleep(1)
