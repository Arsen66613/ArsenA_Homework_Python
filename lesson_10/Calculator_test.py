import pytest
import allure
from CalculatorPage import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка корректного вычисления выражения 7 + 8"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.chrome
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятора"):
        calculator = CalculatorPage(driver)

    with allure.step("Установить задержку вычисления"):
        calculator.delay("45")

    with allure.step("Выполнить вычисление 7 + 8"):
        calculator.click()

    with allure.step("Проверить результат вычисления"):
        screen = calculator.screen()
        assert screen == "15"
