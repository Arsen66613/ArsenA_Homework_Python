import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    if request.node.get_closest_marker("chrome"):
        driver = webdriver.Chrome()
    elif request.node.get_closest_marker("firefox"):
        driver = webdriver.Firefox()
    else:
        raise Exception(
            "Укажи маркер браузера: @pytest.mark.chrome или "
            "@pytest.mark.firefox"
        )

    yield driver
    driver.quit()
