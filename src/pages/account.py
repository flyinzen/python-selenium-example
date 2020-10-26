from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base import BaseEntity


class AccountInfoElement(BaseEntity):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    @property
    def logout_button(self): return self.s('//a[text()="Выйти"]', By.XPATH)

    @property
    def name_label(self): return self.s(
        'div[aria-label="Информация об аккаунте"] div:nth-of-type(2) div:nth-of-type(1)')

    @property
    def email_label(self): return self.s(
        'div[aria-label="Информация об аккаунте"] div:nth-of-type(2) div:nth-of-type(2)')
