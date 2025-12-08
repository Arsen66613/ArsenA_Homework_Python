from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

waiter = WebDriverWait(driver, 10)

# Появление текста "Done!" (все 4 картинки загружены)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

# Выбор из 4-х нужных картинок, исключая логотип
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

third_img = images[2]

print(third_img.get_attribute("src"))

driver.quit()
