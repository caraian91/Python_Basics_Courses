from Tema.tema_11.browser import Browser
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class SecurePage(Browser):
    # Atributs
    MESSAGE_SUCCES_LOGIN = (By.ID, "flash")
    LOGOUT_BTN = (By.XPATH, "//*[contains(text(), 'Logout')]")

    # Methods
    def navigate_to_secure_page(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")

    def verify_message_success_and_displayed(self):
        try:
            actual_msg = self.driver.find_element(*self.MESSAGE_SUCCES_LOGIN).text
        except NoSuchElementException:
            actual_msg = "None"
        expected_msg = "You logged into a secure area!\n×"
        assert actual_msg == expected_msg, f'Error! The message is not diplayed, expected msg {expected_msg}, but the actual is {actual_msg}'

    def logout_button(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()


