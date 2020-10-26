from selenium.webdriver.remote.webdriver import WebDriver

from data.messages import test_message
from run_config import BASE_URL
import data.users as users
from src.pages.pages import PagesMap


def test_send_mail_using_gmail(browser: WebDriver):
    pages = PagesMap(browser)
    pages.login_page.open(BASE_URL).login(users.agent)
    (pages.mail_page.wait_page()
     .check_title(users.agent.email)
     .new_message())
    (pages.new_message
     .write_and_send(test_message))
    pages.mail_page.logout()
    pages.login_page.open(BASE_URL).login(users.bob)
    (pages.mail_page
     .open_message_thread(test_message.subject))
    pages.thread_page.check_message_contains(test_message.subject)
