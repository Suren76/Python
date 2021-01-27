import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.result import BuyAmResultPage


@pytest.mark.usefixtures('add_page_attribute')
@pytest.mark.usefixtures('chrome_driver')
class TestLogoMainBlock:
    def test_logo_link(self):
        self.page.link_button("/html/body/div[1]/header/div/div[3]/div[1]/a")
        assert self.page.current_url == "https://buy.am/hy/"

    def support_info_tell_number(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div[2]/span[1]").text
        assert txt == "+374 11 311 111"

    def support_info_tell_number_text(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div[2]/span[2]").text
        assert txt == "Զանգերի կենտրոն"


@pytest.mark.usefixtures('add_page_attribute')
@pytest.mark.usefixtures('chrome_driver')
class TestShopNavigation:
    def test_navigation_notepad(self):
        self.page.link_button("/html/body/div[1]/header/div/nav/ul/li[3]/a")
        assert self.page.driver.current_url == "https://buy.am/hy/register/index/sTarget/note/sTargetAction/index"

    def test_navigation_cart(self):
        self.page.get()
        self.page.find_element(By.XPATH, "/html/body/div[1]/header/div/nav/ul/li[4]/a")
        button_locat_xpath = "/html/body/div[1]/header/div/nav/ul/li[@class='btn cart--link']"
        assert WebDriverWait(self.page.driver, 5).until(EC.presence_of_element_located(By.XPATH, button_locat_xpath))

    def test_navigation_account(self):
        self.page.find_element(By.XPATH, "/html/body/div[1]/header/div/nav/ul/li[5]/a")
        assert self.page.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/\
        nav/ul/li[@class='navigation--entry entry--account with-slt js--is--dropdown-active']")

    def test_navigation_settings(self):
        self.page.find_element(By.XPATH, "/html/body/div[1]/header/div/nav/ul/li[6]/a")
        assert self.page.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/\
        nav/ul/li[@class='navigation--entry entry--shop-settings is-opened']")


@pytest.mark.usefixtures('add_page_attribute')
@pytest.mark.usefixtures('chrome_driver')
class TestSearchContainer:
    def test_search_category(self):
        self.page.get()

        self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]/div[2]/div').click()
        assert self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]/\
        div[2]/ul[@class="categories-list is-opened"]')

        assert self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]\
        /div[2]/ul/li[2]').text == "Բոլորը"
        assert self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]\
        /div[2]/ul/li[3]').text == "Քարֆուր"
        assert self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]\
        /div[2]/ul/li[1]').text == "Ֆուդկորտ"
        assert self.page.driver.find_element(By.XPATH, '//*[@id="searchCategorySelectionBox"]\
        /div[2]/ul/li[4]').text == "Խանութներ"

    def test_search(self):
        self.page.get()
        self.page_result = BuyAmResultPage(self.driver)

        self.page.search('hot dog')
        assert self.page_result.phrase_result_count('hot dog') > 0
