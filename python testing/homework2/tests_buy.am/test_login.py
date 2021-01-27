import re

import pytest

from pages.login import BuyAmLoginPage, BuyAmRegisterPage


@pytest.mark.usefixtures('chrome_driver')
class TestLogin:
    def test_log_in(self):
        self.page = BuyAmLoginPage(self.driver)
        self.page.get()

        email = "testtest@tmail.am"
        password = ".Test_password_1"

        assert re.search(r"\w+@+[a-z]+.+[a-z]", email)
        self.page.login_email(email)
        print(re.search(r"\w+@+[a-z]+.+[a-z]", email))

        assert re.search(r"\w", password)
        self.page.login_password(password)

        self.page.log_in_account()


@pytest.mark.usefixtures('chrome_driver')
class TestRegistration:
    def test_registration(self):
        self.page = BuyAmRegisterPage(self.driver)
        self.page.get()

        firstname = "Suren"
        assert re.match(r"[a-zA-Z]+", firstname)
        lastname = "Parsyan"
        assert re.match(r"[a-zA-Z]+", lastname)
        email = "testtest@tmail.am"
        assert re.match(r"\w+@+[a-z]+.+[a-z]+", email)
        password = ".Test_password_1"
        assert re.match(r"\w+", password)
        password_confirmation = ".Test_password_1"
        assert re.match(r"\w+", password_confirmation)
        tell_number = "+37412345678"
        assert re.match(r"\+\d+", tell_number)
        city = "Գորիս"
        address = "Bakutnc st. 13"
        assert re.match(r"[a-zA-Z0-9.]+", address)

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
