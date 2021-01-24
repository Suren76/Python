import os

import allure
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@allure.issue('BAS-2432')
def test_basic_duckduckgo_search(browser):
    print(os.environ['URL'])
    PHRASE = 'Armenia'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.get()
    search_page.search(PHRASE)
    result_page = DuckDuckGoResultPage(browser)

    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0

# @allure.feature("Login")
# @allure.story("Login positive")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login():
#     assert True
#
#
# @allure.severity(allure.severity_level.C)
# @allure.feature("Login")
# @allure.story("Login negative")
# def test_login_invalid():
#     assert True
#
#
# @allure.feature("Signup")
# def test_signup():
#     assert True

# @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
# def test_xfail_expected_failure():
#     """this test is an xfail that will be marked as expected failure"""
#     assert False
#
#
# @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
# def test_xfail_unexpected_pass():
#     """this test is an xfail that will be marked as unexpected success"""
#     assert True
#
#
#
# @pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
# def test_skip_by_triggered_condition():
#     pass
