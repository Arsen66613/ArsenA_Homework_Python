import pytest
import allure
from ShopPage import ShopPage


@allure.title("Покупка товаров в магазине")
@allure.description(
    "Проверка полного сценария покупки товаров и итоговой суммы"
)
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.firefox
def test_shop_firefox(driver):
    with allure.step("Открыть страницу магазина"):
        buy = ShopPage(driver)

    with allure.step("Авторизоваться пользователем"):
        buy.authorization_username("standard_user")
        buy.authorization_password("secret_sauce")

    with allure.step("Добавить товары в корзину"):
        buy.add_to_cart()

    with allure.step("Перейти в корзину"):
        buy.shopping_cart()

    with allure.step("Перейти к оформлению заказа"):
        buy.checkout()

    with allure.step("Заполнить данные покупателя"):
        buy.input_first_name("Arsen")
        buy.input_last_name("Avakian")
        buy.input_postal_code("00000")
        buy.button_continue()

    with allure.step("Проверить итоговую сумму заказа"):
        total = buy.summary_total()
        assert total == "Total: $58.29"
