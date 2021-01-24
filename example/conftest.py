import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://buy.am/')

@pytest.hookimpl()
def pytest_sessionstart(session):
    os.environ['URL'] = session.config.getoption("--url")

