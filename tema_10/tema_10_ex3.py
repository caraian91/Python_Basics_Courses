import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import chrome
from selenium.webdriver import ActionChains

class Shop(unittest.TestCase):
    # Atribute
    First_Item = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    Item_in_Cart = (By.XPATH, "//*[@id='shopping_cart_container']/a/span")
    Size_Choise = (By.XPATH, "//*[@id='option-label-size-143-item-167']")
    Color_Choise = (By.XPATH,"//*[@id='option-label-color-93-item-50']")
    Add_Cart = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button")


    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://www.saucedemo.com/")
        self.chrome.find_element(By.XPATH, "//*[@id='user-name']").send_keys('standard_user')
        self.chrome.find_element(By.XPATH, "//*[@id='password']").send_keys('secret_sauce')
        self.chrome.find_element(By.XPATH, "//*[@id='login-button']").click()
    def tearDown(self):
        self.chrome.quit()

    # Test 1 - Check item in cart, verify cart numbers item
    def test_cart(self):
        # choose the first item to add to cart
        self.chrome.find_element(*self.First_Item).click()
        actual_msg = self.chrome.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a/span").text
        expected_msg = '1'
        self.assertEqual(actual_msg, expected_msg, 'Cart number is incorrect')
        sleep(3)
