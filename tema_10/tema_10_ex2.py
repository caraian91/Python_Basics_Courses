import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains


class Shop(unittest.TestCase):
    # Atribute
    First_Item = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[1]/div/a/span")
    Title_item_First_Item = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a")
    Size_Choise_First_Item = (By.XPATH, "//*[@id='option-label-size-143-item-167']")
    Color_Choise_First_Item = (By.XPATH,"//*[@id='option-label-color-93-item-50']")

    Second_Item = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[2]/div/a/span")
    Title_item_Second_Item = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[2]/div/div/strong/a")
    Size_Choise_Second_Item = (By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[2]/div/div/div[3]/div[1]/div/div[3]")
    Color_Choise_Second_Item = (By.XPATH,"//*[@id='option-label-color-93-item-53']")

    Add_Cart_First = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button")
    Add_Cart_Second = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/ol/li[2]/div/div/div[4]/div/div[1]/form/button")

    Next_Btn = (By.XPATH, "//*[@class='button action continue primary']")
    Msg_Warning_No_Data = (By.XPATH, "//*[@id='co-shipping-method-form']/div[3]/span")
    email = (By.ID, "customer-email")
    first_name = (By.XPATH, "//*[@name='firstname']")
    last_name = (By.XPATH, "//*[@name='lastname']")
    street = (By.XPATH, "//*[@name='street[0]']")
    city = (By.XPATH, "//*[@name='city']")
    state = (By.XPATH, "//*[@class='select']/option[4]")
    zip = (By.XPATH, "//*[@name='postcode']")
    country = (By.XPATH, "//*[@name='country_id']/option[236]")
    telephone = (By.XPATH, "//*[@name='telephone']")
    shipping = (By.XPATH, "//*[@id='checkout-shipping-method-load']/table/tbody/tr[1]/td[1]/input")

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(10)
        self.firefox.get("https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html")

    def tearDown(self):
        self.firefox.quit()

    # Test 1 - Check item in cart, verify cart message
    def test_cart(self):
        # hover the product
        first_prduct = self.firefox.find_element(*self.First_Item)
        ActionChains(self.firefox).move_to_element(first_prduct).perform()

        # first product choose the size, color and add to cart
        self.firefox.find_element(*self.Size_Choise_First_Item).click()
        self.firefox.find_element(*self.Color_Choise_First_Item).click()
        self.firefox.find_element(*self.Add_Cart_First).click()
        sleep(3)

        # check if the message that it has been added to the basket appears
        product_title = self.firefox.find_element(*self.Title_item_First_Item).text
        actual_msg = self.firefox.find_element(By.XPATH,"//*[@id='maincontent']/div[2]/div[2]/div/div").text
        expected_msg = f'You added {product_title} to your shopping cart.'
        self.assertEqual(actual_msg, expected_msg, 'Cart message is incorrect')

    # Test 2 - Check price from product description with price from cart
    def test_price_quantity_cart(self):
        self.test_cart()
        self.firefox.find_element(By.XPATH, "//*[@class='action showcart']").click()
        first_product_price = self.firefox.find_element(By.XPATH, "//*[@id='product-price-430']/span").text
        total_price = self.firefox.find_element(By.XPATH, "//*[@id='minicart-content-wrapper']/div[2]/div[2]/div/span/span").text
        self.firefox.find_element(By.XPATH, "//*[@id='top-cart-btn-checkout']").click()
        self.assertEqual(first_product_price, total_price, 'The price doesn`t match')


    # Test 3 - Verify proceed to checkout - whitout complete the Shipping Address
    def test_checkout_not_filled(self):
        self.test_cart()
        self.firefox.find_element(By.XPATH, "//*[@class='action showcart']").click()
        sleep(1)
        self.firefox.find_element(By.XPATH, "//*[@id='top-cart-btn-checkout']").click()
        sleep(3)
        self.firefox.find_element(*self.Next_Btn).click()
        actual_msg = self.firefox.find_element(*self.Msg_Warning_No_Data).text
        expected_msg = "The shipping method is missing. Select the shipping method and try again."
        self.assertEqual(actual_msg,expected_msg,"The shipping form is not completed")


    # Test 4 - Verify proceed to checkout - complete the Shipping Address
    def test_checkout_filled_out(self):
        self.test_cart()
        self.firefox.find_element(By.XPATH, "//*[@class='action showcart']").click()
        sleep(1)
        self.firefox.find_element(By.XPATH, "//*[@id='top-cart-btn-checkout']").click()
        sleep(3)
        self.firefox.find_element(*self.first_name).send_keys("Cristi")
        self.firefox.find_element(*self.last_name).send_keys("Pop")
        self.firefox.find_element(*self.street).send_keys("Str.Anton Mihalcea Nr.12")
        self.firefox.find_element(*self.city).send_keys("New York")
        self.firefox.find_element(*self.state).click()
        self.firefox.find_element(*self.zip).send_keys("12345")
        self.firefox.find_element(*self.country).click()
        self.firefox.find_element(*self.telephone).send_keys("0232112455")
        self.firefox.find_element(*self.shipping).click()
        self.firefox.find_element(*self.email).send_keys("abc@gmail.com")
        self.firefox.find_element(*self.Next_Btn).click()
        sleep(5)


