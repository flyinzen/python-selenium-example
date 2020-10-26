from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from src.dto.user import User
from src.pages.account import AccountInfoElement
from src.pages.base import BaseEntity
from src.pages.new_message import NewMessage
from src.util.helpers import wait


class MailListPage(BaseEntity):

    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.account_popup = AccountInfoElement(self.browser)

    @property
    def write_button(self): return self.s('//div[text()="Написать"]', By.XPATH)

    @property
    def inbox_button(self): return self.s('a[aria-label="Входящие"]')

    @property
    def email_list(self): return self.ss('//span[@data-thread-id]/../../..', By.XPATH)

    @property
    def name_label(self): return self.s('a[aria-label*="Аккаунт Google:"]')

    @property
    def change_account_button(self):
        return self.s('//div[text()="Сменить аккаунт"]', By.XPATH)

    def email_item(self, text: str):
        return self.s(f'//span[@data-thread-id][text()="{text}"]/../../../../tr')

    def wait_page(self):
        wait(lambda: self.write_button.is_displayed())
        return self

    def check_title(self, email: str):
        assert f'Входящие - {email} - Gmail' in self.browser.title
        return self

    def opened(self, user: User):
        self.check_title(user.email)
        self.write_button.is_displayed()
        self.inbox_button.is_displayed()
        self.email_list.is_displayed()
        self.name_label.is_displayed()
        return False

    def logout(self):
        self.name_label.click()
        self.account_popup.logout_button.click()
        self.change_account_button.click()
        return self

    def open_message_thread(self, subject: str):
        self.email_item(subject).click()
        return self

    def new_message(self):
        self.write_button.click()
        return NewMessage(self.browser)
