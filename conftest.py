import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        choices=("chrome", "edge", "firefox", "yandex"),
        help="Choose browser",
    )


@pytest.fixture
def driver(request):
    # Сначала проверяем маркер
    marker_browser = None
    for mark in request.node.iter_markers():
        if mark.name in ("chrome", "firefox", "edge", "yandex"):
            marker_browser = mark.name
            break

    # Если маркер есть — используем его, иначе берем из CLI
    browser = marker_browser or request.config.getoption("--browser")
    if browser is None:
        browser = "chrome"  # дефолт

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "edge":
        service = EdgeService(
            executable_path=(
                r"D:\SkyPro\Курс5-Python\edgedriver_win64\msedgedriver.exe")
                )
        driver = webdriver.Edge(service=service)

    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        options.binary_location = (
            r"C:\Users\Public\Yandex\YandexBrowser\Application\browser.exe"
        )
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
