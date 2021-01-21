import pytest
from selenium import webdriver
from datetime import datetime


@pytest.fixture(scope="class")
def chrome_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--add-text", action="store", default="new todo", help="Added text")


@pytest.fixture
def add_text(request):
    return request.config.getoption("--add-text")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome == 'failed':
        item.cls.driver.get_screenshot_as_file(f"./fail_{item.name}_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.png")