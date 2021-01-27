from pages.basepage import BasePage
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('chrome_driver')
class TestBtn:
    def test_get(self):
        self.page = BasePage(self.driver)
        self.page.get()


        self.page.link_button(button_locat_xpath="/html/body/div[1]/header/div/nav/ul/li[3]/a")
        assert self.page.driver.current_url == "https://buy.am/hy/register/index/sTarget/note/sTargetAction/index"

