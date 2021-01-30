import pytest
import allure
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('add_page_attribute')
@pytest.mark.usefixtures('chrome_driver')
class TestSection:
    def test_banner_slider(self):

        slider_elm = self.page.driver.find_elements(By.XPATH, "//section/div[3]/div/div/div/div")
        assert len(slider_elm) == 5

    def test_wishlist_button(self):
        @allure.story("Login negative")
        if self.page.find_element(By.XPATH, "//nav/ul/li[5]/div/div[2]/div/ul/li[7]/a").text == 'Մուտք':
            self.page.driver.find_element(By.XPATH, "//section/div/div/div/div\
            /div[1]/section/div[2]/div/div/div/div/div/div/form/button").click()

        assert self.page.driver.current_url == "https://buy.am/hy/register/index/sTarget/note/sTargetAction/index"

        @allure.story("Login positive")
        if self.page.find_element(By.XPATH, "//nav/ul/li[5]/div/div[2]/div/ul/li[7]/a/span").text == 'Դուրս գալ':
            self.page.driver.find_element(By.XPATH, "//section/div/div/div/div\
            /div[1]/section/div[2]/div/div/div/div/div/div/form/button").click()

            assert self.page.driver.current_url == "https://buy.am/hy/note"

    def test_add_busket_button(self):
        busket_len_before = int(self.page.driver.find_element(By.XPATH, "//header/div/nav/ul/li[4]/a/span").text)

        self.page.driver.find_element(By.XPATH, "//section/div/div/div/div\
        /div[1]/section/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/form/button").click()

        basket_len_after = int(self.page.driver.find_element(By.XPATH, "//header/div/nav/ul/li[4]/a/span").text)

        assert busket_len_before + 1 == basket_len_after
