from Tema.tema_11.browser import Browser
from selenium.webdriver.common.by import By

class HomePage(Browser):
    # Atributs
    ADD_AND_REMOVE_PAGE = (By.LINK_TEXT, "Add/Remove Elements")
    CONTEXT_MENU_PAGE = (By.LINK_TEXT, "Context Menu")
    FORM_AUTHENTICATION_PAGE = (By.LINK_TEXT, "Form Authentication")

    # Methods
    def home_page(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def navigate_to_add_remove_page(self):
        self.driver.find_element(*self.ADD_AND_REMOVE_PAGE).click()

    def navigate_to_context_menu_page(self):
        self.driver.find_element(*self.CONTEXT_MENU_PAGE).click()

    def navigate_to_form_authentication_page(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION_PAGE).click()