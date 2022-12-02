from Tema.tema_11.browser import Browser
from selenium.webdriver.common.by import By

class LoginPage(Browser):
    # Atributs
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//*[@type='submit']")

    # Methods
    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def set_username(self,user):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user)

    def set_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def login_button(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

