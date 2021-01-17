import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    d_chrome = webdriver.Chrome()
    yield d_chrome
    d_chrome.quit()
