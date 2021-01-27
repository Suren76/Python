import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('add_page_attribute')
@pytest.mark.usefixtures('chrome_driver')
class TestNavigationBlock:
    def test_menu_items_hover(self):
        hover = ActionChains(self.page.driver).move_to_element

        elm_1 = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div[1]/ul/li[1]/div")
        hover(elm_1).perform()
        parm_1 = "//div[1]/nav/div/div[1]/ul/li[1][@class='navigation--entry js--menu-scroller--item is--hovered']"
        parm_2 = '//nav/div/div[2][@class="advanced-menu is-opened"]/div[1][@class="menu--container menu--is-active"]'
        assert self.page.driver.find_element(By.XPATH, parm_1) and self.page.driver.find_element(By.XPATH, parm_2)

        elm_2 = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div[1]/ul/li[2]/div")
        hover(elm_2).perform()
        parm_1 = "//div[1]/nav/div/div[1]/ul/li[2][@class='navigation--entry js--menu-scroller--item is--hovered']"
        parm_2 = '//nav/div/div[2][@class="advanced-menu is-opened"]/div[2][@class="menu--container menu--is-active"]'
        assert self.page.driver.find_element(By.XPATH, parm_1) and self.page.driver.find_element(By.XPATH, parm_2)

        elm_3 = self.page.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div[1]/ul/li[3]/div")
        hover(elm_3).perform()
        parm_1 = "//div[1]/nav/div/div[1]/ul/li[3][@class='navigation--entry js--menu-scroller--item is--hovered']"
        parm_2 = '//nav/div/div[2][@class="advanced-menu is-opened"]/div[3][@class="menu--container menu--is-active"]'
        assert self.page.driver.find_element(By.XPATH, parm_1) and self.page.driver.find_element(By.XPATH, parm_2)

    # 1    Սուպերմարկետ

    def test_advanced_menu_item_1(self):
        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/bakery-pastry"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/fresh-fruit-vegetable"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/ready-meals"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/fresh-meat"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/fish-seafood"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/sausages"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[1]/li[7]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/frozen-products"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/dairy-eggs"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/breakfast-coffee-tea"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/bio-organic"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/sweets-snacks"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/grocery"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/juices-drinks"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[2]/li[7]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/alcoholic-beverages-cigarettes"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/babys-accessories-food"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/hygiene-supplies"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/household-goods"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/pet-food"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/clothes-and-shoes"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/shop-in-shop"

        self.page.get()
        self.page.link_button("//div[2]/div[1]/div/ul[3]/li[7]")
        assert self.page.driver.current_url == "https://buy.am/hy/carrefour/sales"

    # 2   Ֆուդկորտ

    def test_advanced_menu_item_2(self):
        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[1]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/sales-and-special-offers"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[1]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/lunch-time"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[1]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/salads"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[1]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/dough-dishes"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[2]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/fast-food"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[2]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/barbecue"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[2]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/seafood"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[2]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/halfstuff"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[3]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/fresh-coffee-tea-icecream"

        self.page.get()
        self.page.link_button("//div[2]/div[2]/div/ul[3]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/food-court/sweets"

    # 3    Խանութներ
    def test_advanced_menu_item_3(self):
        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/electronics-home-appliances"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/cell-phones-accessories"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/clothing-accessories"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/perfume-cosmetics-care-products"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/jewelry-accessories"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/flowers-accessories"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[1]/li[7]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/shoes-bags"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/eyewear-lenses"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/books"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/office-stationery-supplies"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/kids-world"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/sporting-goods"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/household-essentials-beauty-products"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[2]/li[7]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/alcoholic-beverages"

        ####

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[1]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/cigarettes-tobaccorelated-products"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[2]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/garden-construction-tools"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[3]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/medical-equipment-and-accessories"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[4]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/gift-cards"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[5]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/coffee-tea-spices"

        self.page.get()
        self.page.link_button("//div[2]/div[3]/div/ul[3]/li[6]")
        assert self.page.driver.current_url == "https://buy.am/hy/shops/pet-food-accessories"
