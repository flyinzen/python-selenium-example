from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.dto.message import Message
from src.pages.base import BaseEntity


class NewMessage(BaseEntity):
    @property
    def address(self): return self.s('textarea[aria-label="Кому"]')

    @property
    def subject(self): return self.s('input[aria-label="Тема"]')

    @property
    def message(self): return self.s('div[aria-label="Тело письма"]')

    @property
    def send(self): return self.s('//div[text()="Отправить"]', By.XPATH)

    def write_and_send(self, message: Message):
        self.address.send_keys(message.to)
        self.subject.send_keys(message.subject)
        self.message.send_keys(message.body)
        self.send.click()
        return self
