from time import sleep
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome_driver")
class TestLambdatestTodoApp:

    def test_page(self):
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        assert "Sample page - lambdatest.com" == self.driver.title

    def test_item_add(self, cmdopt):
        li_len_before = len(self.driver.find_elements_by_tag_name("li"))

        self.driver.find_element_by_id("sampletodotext").send_keys("new book")
        self.driver.find_element_by_id("addbutton").click()
        self.driver.find_element_by_id("sampletodotext").send_keys(cmdopt)
        self.driver.find_element_by_id("addbutton").click()

        add_todo = ["new book", cmdopt]

        li_len_after = len(self.driver.find_elements_by_tag_name("li"))
        assert li_len_before + len(add_todo) == li_len_after

    def test_todo_done(self):
        self.driver.find_element(By.XPATH, '//li[2]/input').click()
        assert self.driver.find_element(By.XPATH, '//li[2]/span[@class="done-true"]')
        sleep(2)

    @pytest.mark.skip
    def test_fail(self):
        assert False