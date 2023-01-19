import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_OpenLink_Positif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html") 
        driver.maximize_window()
        response_massage= driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(response_massage,'Epic sadface: You can only access '+'/inventory.html'+ 'when you are logged in.')

    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_massage= driver.find_element(By.CSS_SELECTOR,"#header_container > div.header_secondary_container > span").text
        self.assertEqual(response_massage,'PRODUCTS')

    def test_Login_Negatif(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("a")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("a")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_massage= driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertEqual(response_massage,'Epic sadface: Username and password do not match any user in this service')


unittest.main()