from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    edge_driver_path = (
        r"D:\SkyPro\Курс5-Python\edgedriver_win64\msedgedriver.exe"
        )
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 10)

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Ищем кнопку по классам
    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")
        )
    )

    # Проверяем видимость (например, если в параметрах экрана масштаб > 100%)
    if submit_btn.is_displayed():
        submit_btn.click()
    else:
        raise Exception("Кнопка не кликабельна!")

    # Проверка, что заполненные поля подсвечиваются зелёным
    GREEN = "rgba(209, 231, 221, 1)"  # #d1e7dd в rgba

    # Проверка, что незаполненные поля подсвечиваются красным
    RED = "rgba(248, 215, 218, 1)"    # #f8d7da в rgba

    filled_fields = [
        "first-name", "last-name", "address", "city", "country",
        "e-mail", "phone", "job-position", "company"
    ]

    for id in filled_fields:
        elem = driver.find_element(By.ID, id)
        bg_color = elem.value_of_css_property("background-color")
        assert bg_color == GREEN

    # Проверяем пустое поле zip-code
    zip_elem = driver.find_element(By.ID, "zip-code")
    zip_color = zip_elem.value_of_css_property("background-color")
    assert zip_color == RED

    driver.quit()
