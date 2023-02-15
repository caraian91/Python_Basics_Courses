import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
class Shop(unittest.TestCase):
    # Atributs
    TOP_MENU_ELECTRONICS = (By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
    ELECTRONIC_SUBMENU_CELLPHONES = (By.XPATH,"//*[@class='top-menu notmobile']//a[normalize-space()='Cell phones']")
    FIRST_ITEM_CART = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    SECOND_ITEM_CART = (By.XPATH, "(//button[text()='Add to cart'])[2]")
    PRICE_FIRST_ITEM = (By.XPATH, "(//*[@class='price actual-price'])[1]")
    PRICE_SECOND_ITEM = (By.XPATH, "(//*[@class='price actual-price'])[2]")
    MESSAGE_CARD_ADDED = (By.XPATH, "//*[@id='bar-notification']/div/p")
    CLOSE_MESSAGE_CARD_ADDED = (By.CLASS_NAME, "close")
    PRICE_FROM_CART = (By.XPATH, "//div[@class='price']//span[1]")
    SHOPPING_CART = (By.CLASS_NAME, "cart-label")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://demo.nopcommerce.com/")

    def tearDown(self):
        self.chrome.quit()

    # Test 1 - Navigate to page CellPhones
    def test_navigate_page_cellphones(self):
        # hover menu
        hover_submenu = self.chrome.find_element(*self.TOP_MENU_ELECTRONICS)
        action = ActionChains(self.chrome)
        action.move_to_element(hover_submenu).perform()
        # click CellPhones
        self.chrome.find_element(*self.ELECTRONIC_SUBMENU_CELLPHONES).click()
        # check the new url
        actual_url = self.chrome.current_url
        expected_url = "https://demo.nopcommerce.com/cell-phones"
        self.assertEqual(actual_url, expected_url, 'URL is incorrect')
        sleep(3)

    # Test 2 - Insert item in cart, verify cart message
    def test_cart(self):
        self.test_navigate_page_cellphones()
        self.chrome.find_element(*self.FIRST_ITEM_CART).click()
        actual_msg = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.MESSAGE_CARD_ADDED)).text
        expected_msg = "The product has been added to your shopping cart"
        self.assertEqual(actual_msg,expected_msg,f"Error the product is not in the shopping cart!. No message {expected_msg}")


    # Test 3 - Verify price from product description with price from cart
    def test_price_cart(self):
        self.test_cart()
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(*self.CLOSE_MESSAGE_CARD_ADDED).click()

        price_first_item = self.chrome.find_element(*self.PRICE_FIRST_ITEM).text
        shop_cart = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SHOPPING_CART))
        hover_shop_cart = ActionChains(self.chrome).move_to_element(shop_cart).perform()
        price_from_the_cart = self.chrome.find_element(*self.PRICE_FROM_CART).text
        print(price_first_item,"as")
        print(price_from_the_cart)
        # assert price_first_item == price_from_the_cart, f"The price are not equal, price item {price_from_the_cart} and the price from cart {price_from_the_cart}"
        sleep(3)