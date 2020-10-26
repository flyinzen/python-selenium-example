import time

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from run_config import WAIT_TIMEOUT, POOL_TIMEOUT


def wait(condition, expected=True):
    end_time = time.time() + WAIT_TIMEOUT
    res = condition() == expected
    while not res and time.time() < end_time:
        time.sleep(POOL_TIMEOUT)
        res = condition() == expected
    return res

