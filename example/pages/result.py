from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class DuckDuckGoResultPage(BasePage):
    LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

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