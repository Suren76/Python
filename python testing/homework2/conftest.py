from datetime import datetime
from os import environ
from pages.basepage import BasePage

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome == 'failed':
        pass
        item.cls.driver.get_screenshot_as_file(
            f"./fail_{item.name}_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.png")


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://buy.am/')


@pytest.hookimpl()
def pytest_sessionstart(session):
    environ['URL'] = session.config.getoption("--url")


@pytest.fixture(scope="class")
def add_page_attribute(request):
    page = BasePage(request.cls.driver)
    request.cls.page = page
