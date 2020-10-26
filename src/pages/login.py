from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.dto.user import User
from src.pages.base import BaseEntity


class GmailLoginPage(BaseEntity):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)

    @property
    def username_input(self):
        return self.s('input[name="identifier"]')

    @property
    def next_button(self):
        return self.s('div[id*="Next"] button')

    @property
    def password_input(self):
        return self.s('input[name="password"]')



    def open(self, url: str):
        self.browser.get(url)
        return self

    def login(self, user: User):
        self.username_input.send_keys(user.email)
        self.next_button.click()
        self.password_input.send_keys(user.password)
        try:
            self.next_button.click()
        except StaleElementReferenceException:
            self.next_button.click()
        return self

