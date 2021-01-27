from pages import basepage
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('chrome_driver')
class TestFirstBlock:
    def test_new_letters_title(self):
        self.page = basepage.BasePage(self.driver)
        self.page.get()
        footer_title = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[1]/div[1]/p").text
        assert footer_title == 'Բաժանորդագրվեք մեր առաջարկներին'
    
    def test_newsletter_field(self):
        self.page.get()
        self.page.driver.find_element(By.CLASS_NAME, "newsletter--field").send_keys("test@test.am")
        self.page.link_button("/html/body/div[1]/footer/div/div/div[1]/div[1]/form/button")
        assert self.page.driver.current_url == 'https://buy.am/hy/newsletter'

    def test_logo_link(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[1]/div[2]/a")
        assert self.page.driver.current_url == "https://buy.am/hy/"

    def test_footer_copyright(self):
        self.page.get()
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[1]/div[2]/p").text
        assert txt == " \
        © 2011–2021 - BUY.AM, ՀՀ, Ք. ԵՐԵՎԱՆ, 0001, ԱՎԱԳ ՊԵՏՐՈՍՅԱՆ 4, (+374) 11 31 11 11\
        BUY.AM-Ի ՏԵԽՆԻԿԱԿԱՆ ՍՊԱՍԱՐԿՄԱՆ ԹԻՄ. ԿԱՆԴԵԼԼԱ ՍՊԸ, ՏԴ ԿՈՆՍԱԼՏԻՆԳ, ԲԻԶՆԵՍ ԼՈՋԻՔ ՍՊԸ\
        ԿԱՅՔԻ ԲՈԼՈՐ ԻՐԱՎՈՒՆՔՆԵՐԸ ՊԱՏԿԱՆՈՒՄ ԵՆ ԿԱՆԴԵԼԼԱ ՍՊ ԸՆԿԵՐՈՒԹՅԱՆԸ\
        "

@pytest.mark.usefixtures("chrome_driver")
class TestFooterMenu:
    def test_footer_menu_title(self):
        self.page = basepage.BasePage(self.driver)
        self.page.get()
        assert self.page.driver.title == ""

    def test_footer_nav_link_1(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[2]/div/nav/ul/li[1]/a")
        assert self.page.driver.current_url == 'https://buy.am/hy/custom/index/sCustom/52'

    def test_footer_nav_link_2(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[2]/div/nav/ul/li[2]/a")
        assert self.page.driver.current_url == 'https://buy.am/hy/custom/index/sCustom/51'

    def test_footer_nav_link_3(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[2]/div/nav/ul/li[3]/a")
        assert self.page.driver.current_url == 'https://buy.am/hy/custom/contact'

    def test_footer_nav_link_4(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[2]/div/nav/ul/li[4]/a")
        assert self.page.driver.current_url == 'https://buy.am/hy/custom/index/sCustom/50'

@pytest.mark.usefixtures("chrome_driver")
class TestAssocatationsBlock:
    
    def test_get(self):
        self.page = basepage.BasePage(self.driver)
        self.get()


    def test_fb(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[3]/div/ul[1]/li[1]/a")
        assert self.page.driver.current_url == 'https://www.facebook.com/BuyamOnlineMall/'

    def test_instagram(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[3]/div/ul[1]/li[2]/a")
        assert self.page.driver.current_url == 'https://www.instagram.com/buy.am_onlinemall/'

    def test_youtube(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[3]/div/ul[1]/li[3]/a")
        assert self.page.driver.current_url == 'https://www.youtube.com/user/buyamofficial'
        


    def test_visa(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[2]/li[1]").text
        assert txt == "visa" 

    def test_master(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[2]/li[2]").text
        assert txt == "master" 
 
    def test_arca(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[2]/li[3]").text
        assert txt == "arca" 



    def test_idram(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[3]/li[1]").text
        assert txt == "idram" 

    def test_mobidram(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[3]/li[2]").text
        assert txt == "mobidram" 

    def test_payx(self):
        txt = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/footer/div/div/div[3]/div/ul[3]/li[3]").text
        assert txt == "payx" 



    def test_google_play(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[3]/div/ul[4]/li[1]/a")
        assert self.page.driver.current_url == 'https://play.google.com/store/apps/details?id=com.candella.buyam'

    def test_app_store(self):
        self.page.link_button("/html/body/div[1]/footer/div/div/div[3]/div/ul[4]/li[2]/a")
        assert self.page.driver.current_url == 'https://itunes.apple.com/app/buy-am/id1224598831'

 