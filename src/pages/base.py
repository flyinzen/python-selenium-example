from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from run_config import WAIT_TIMEOUT
from src.util.helpers import wait
from src.util.logger import get_logger

log = get_logger(__name__)


class BaseEntity:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def s(self, locator: str, by=By.CSS_SELECTOR) -> WebElement:
        try:
            element = WebDriverWait(self.browser, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((by, locator)),
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            assert False, f'element {(by, locator)} not found during {WAIT_TIMEOUT} sec'
        return element

    def ss(self, locator: str, by=By.CSS_SELECTOR):
        return self.browser.find_elements(by, locator)

    def wait_page(self):
        wait(lambda: 'Gmail' in self.browser.title)
        return self
