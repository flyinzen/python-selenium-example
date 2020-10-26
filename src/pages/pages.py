from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.account import AccountInfoElement
from src.pages.base import BaseEntity
from src.pages.login import GmailLoginPage
from src.pages.mail import MailListPage
from src.pages.new_message import NewMessage
from src.pages.thread import MessagesThreadPage


class PagesMap:
    def __init__(self, browser: WebDriver):
        self.base_page = BaseEntity(browser)
        self.account_page = AccountInfoElement(browser)
        self.login_page = GmailLoginPage(browser)
        self.mail_page = MailListPage(browser)
        self.new_message = NewMessage(browser)
        self.thread_page = MessagesThreadPage(browser)
