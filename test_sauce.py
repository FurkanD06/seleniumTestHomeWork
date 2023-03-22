from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Sauce_Test:
    def username_and_password_null(self):
        driver =webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        loginBtn =driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(10)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")


    def password_null(self):
        driver =webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        username_input = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        sleep(2)
        username_input.send_keys("theDone")
        sleep(2)

        loginBtn =driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(10)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text=="Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")

    def user_locked(self):
        driver =webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernama_input = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        usernama_input.send_keys("locked_out_user")
        sleep(2)
        password_input = driver.find_element(By.ID,"password")
        password_input.send_keys("secret_sauce")

        loginBtn =driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(10)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    def click_icon(self):
        driver =webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        loginBtn =driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(10)

        errorBtn=driver.find_element(By.CLASS_NAME,"error-button")
        sleep(2)
        errorBtn.click()
        sleep(10)


    def username_passwrod_true(self):
           driver =webdriver.Chrome(ChromeDriverManager().install())
           driver.maximize_window()
           driver.get("https://www.saucedemo.com/")
           sleep(5)
           usernama_input = driver.find_element(By.ID,"user-name")
           sleep(2)
           usernama_input.send_keys("standard_user")
           sleep(2)
           password_input = driver.find_element(By.ID,"password")
           sleep(5)
           password_input.send_keys("secret_sauce")
           sleep(2)

           loginBtn =driver.find_element(By.ID,"login-button")
           sleep(2)
           loginBtn.click()
           sleep(10)

           productList = driver.find_elements(By.CLASS_NAME, "inventory_item") 
           print(f"Ürün : {len(productList)}")
           sleep(20)


testClass = Sauce_Test()
testClass.username_and_password_null()
testClass.password_null()
testClass.user_locked()
testClass.username_passwrod_true() 
testClass.click_icon()