from datetime import datetime
from os import environ

import allure
import pytest
from pages.basepage import BasePage
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
        allure.attach(f"fail_{item.name}_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.png",
                      item.cls.driver.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://buy.am/')


@pytest.hookimpl()
def pytest_sessionstart(session):
    environ['URL'] = session.config.getoption("--url")


@pytest.fixture(scope="class")
def add_page_attribute(request):
    page = BasePage(request.cls.driver)
    request.cls.page = page
