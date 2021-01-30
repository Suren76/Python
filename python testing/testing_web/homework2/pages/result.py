from selenium.webdriver.common.by import By

from .basepage import BasePage


class BuyAmResultPage(BasePage):
    LINK_DIVS = (By.CSS_SELECTOR, ".listing > div")
    SEARCH_INPUT = (By.NAME, 'sSearch')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//div[@class='listing']//div[@data-category-id='2']//*[contains(text(), '{phrase}')]"
        return By.XPATH, xpath

    def __init__(self, driver):
        super().__init__(driver)

    def link_div_count(self):
        link_divs = self.driver.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        phrase_results = self.driver.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
