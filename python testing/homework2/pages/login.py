from selenium.webdriver.common.by import By

from .basepage import BasePage


class BuyAmLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = "hy/register/index/sTarget/note/sTargetAction/index"

    def login_email(self, email):
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(str(email))

    def login_password(self, password):
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(str(password))

    def log_in_account(self):
        self.driver.find_element(By.XPATH, "//button[@class='register--login-btn btn is--primary is--large']").click()


class BuyAmRegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = "hy/register/index/sTarget/note/sTargetAction/index"

    def register_personal_salutation(self, salutation):
        xpath = "//select[@id = 'salutation']"
        self.driver.find_element(By.XPATH, xpath).click()
        self.driver.find_element(By.XPATH, xpath + f"/option[@value={salutation}]").click()

    def register_firstname(self, first_name):
        self.driver.find_element(By.NAME, "register[personal][firstname]").send_keys(first_name)

    def register_lastname(self, last_name):
        self.driver.find_element(By.NAME, "register[personal][lastname]").send_keys(last_name)

    def register_email(self, email):
        self.driver.find_element(By.NAME, "register[personal][email]").send_keys(email)

    def register_password(self, password):
        self.driver.find_element(By.NAME, "register[personal][password]").send_keys(password)

    def register_password_confirmation(self, password_confirmation):
        self.driver.find_element(By.NAME, "register[personal][passwordConfirmation]").send_keys(password_confirmation)

    def register_phone(self, phone):
        self.driver.find_element(By.NAME, "register[personal][phone]").send_keys(phone)

    def register_city_select(self, city):
        self.driver.find_element(By.NAME, "register[billing][country_state_57]").click()
        self.driver.find_element(By.XPATH,
                                 f'//select[@name="register[billing][country_state_57]"]'
                                 f'/option//*[contains(text(), "{city}")]').click()

    def register_address(self, address):
        self.driver.find_element(By.NAME, "register[billing][street]").send_keys(address)

    def register_account(self):
        self.driver.find_element(By.XPATH, "//div[@class='register--action']/button").click()
