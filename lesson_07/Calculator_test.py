import pytest
from CalculatorPage import CalculatorPage


@pytest.mark.chrome
def test_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.delay('45')

    calculator.click()

    screen = calculator.screen()

    assert screen == '15'

    driver.quit()
