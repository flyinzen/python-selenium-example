import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from run_config import BROWSER
from src.util.logger import get_logger

log = get_logger(__name__)


@pytest.fixture(scope='function')
def browser() -> WebDriver:
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        pytest.exit(f'unsupported browser {BROWSER} in configuration', 3)
    yield driver
    driver.quit()
