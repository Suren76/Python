from pages.login import BuyAmLoginPage,BuyAmRegisterPage
from pages.basepage import BasePage
import re
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures('chrome_driver')
class TestLogin:
    def test_get(self):
        self.page = BuyAmLoginPage(self.driver)
        self.page.get()

    def test_log_in(self):
        email = "testtest@tmail.am"
        password = ".Test_password_1"

        assert re.search(r"\w+@+[a-z]+.+[a-z]",email)
        self.page.login_email(email)

        assert re.search(r"\w",password)
        self.page.login_password(password)

        self.page.log_in_account()


@pytest.mark.usefixtures('chrome_driver')
class TestRegistration:
    def test_get(self):
        self.page = BuyAmRegisterPage(self.driver)
        self.page.get()


    def test_registration(self):

        firstname = "Suren"
        assert re.search(r"[a-zA-Z]",firstname)
        lastname = "Parsyan"
        assert re.search(r"[a-zA-Z]",lastname)
        email = "testtest@tmail.am"
        assert re.search(r"\w+@+[a-z]+.+[a-z]",email)
        password = ".Test_password_1"
        assert re.search(r"\w",password)
        password_confirmation = ".Test_password_1"
        assert re.search(r"\w",password_confirmation)
        tell_number = "+37412345678"
        assert re.search(r"\+\d",tell_number)
        city = "Գորիս"
        address = "Bakunc st. 13"
        assert re.search(r"[a-zA-Z0-9.]",address)

        self.page.register_personal_salutation("Mr")
        self.page.register_firstname(firstname)
        self.page.register_lastname(lastname)
        self.page.register_email(email)
        self.page.register_password(password)
        self.page.register_password_confirmation(password_confirmation)
        self.page.register_phone(tell_number)
        self.page.register_city_select(city)
        self.page.register_address(address)
        self.page.register_account()

