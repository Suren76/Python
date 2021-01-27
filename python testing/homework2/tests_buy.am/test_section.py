from pages.basepage import BasePage
import pytest
from selenium.webdriver.common.by import By


class TestSection:
    def test_get(self):
        self.page = BasePage(self.driver)
        self.page.get()

    def test_banner_slider(self):

        slider_elm = self.page.driver.find_elements(By.XPATH, "//section/div[3]/div/div/div/div")
        assert len(slider_elm) == 5

    def test_product_block(self):
        def test_wishlist_button(self):
            # not log in
            self.page.driver.find_element(By.XPATH, "//section/div/div/div/div\
            /div[1]/section/div[2]/div/div/div/div/div/div/form/button").click()

            assert self.page.driver.current_url == "https://buy.am/hy/register/index/sTarget/note/sTargetAction/index"

            # logged in

        def test_add_busket_button(self):
            busket_len_before = int(self.page.driver.find_element(By.XPATH, "//header/div/nav/ul/li[4]/a/span").text)
            
            self.page.driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/div\
            /div[1]/section/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/form/button").click()
            
            busket_len_afther = int(self.page.driver.find_element(By.XPATH, "//header/div/nav/ul/li[4]/a/span").text)
            
            assert busket_len_before+1 == busket_len_afther