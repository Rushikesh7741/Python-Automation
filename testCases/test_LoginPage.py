import pytest
from selenium import webdriver
from time import sleep

from  PageObjects.LoginPage import LoginPage
from PageObjects.Product import Product
from testCases.Conftest import setup
from Utilities.readproperties import readcongig
class Test_001_Login:
 baseURL=readcongig.getApplicationURL()
 username=readcongig.getUsername()
 password=readcongig.getPassword()
 def test(self, setup):
     self.driver =setup
     self.driver.get(self.baseURL)
     act_title=self.driver.title

     if act_title== "Swag Labs" :
         assert True
     else:
         self.driver.save_screenshot(".//Screenshots//"+"test.png")
         assert False


 def test_login(self,setup):
     self.driver=setup
     self.driver.get(self.baseURL)
     self.lp=LoginPage(self.driver)
     self.lp.setUserName(self.username)
     self.lp.setPassword(self.password)
     self.lp.clickLoginButton()
     act_title=self.driver.title
     if act_title=="Swag Labs":
         assert  True
     else:
         self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
         assert False
    #  self.pd=Product(self.driver)
    #  self.pd.Shopping_cart()
    # #     add product
    # pass
    # verfy count
    # self.verify_count(1)
 #
 # def test_Add_Product(self,setup):
 #     self.driver=setup
 #     self.driver.get(self.baseURL)
 #     sleep(2)
 #     self.lp=LoginPage(self.driver)
 #     sleep(2)
 #     self.lp.setUserName(self.username)
 #     sleep(2)
 #     self.lp.setPassword(self.password)
 #     sleep(2)
 #     self.lp.clickLoginButton()
 #     sleep(2)
 #     self.pd=Product(self.driver)
 #     productName= 'Sauce Labs Backpack'
 #     self.pd.add_product_click(productName)
 #     self.pd.verify_count(1)
 #     sleep(2)
 #     self.pd.Shopping_cart()
 #     sleep(2)
 #     # self.pd.verify_count(1)
 #     # sleep(2)
 #     self.pd.Verify_Products()
 #     sleep(2)
 #     # productsList = self.pd.get_product_list_from_cart()
 #     # #
 #     # assert productName in productsList,"error msg"
 #     # sleep(2)
 #     # self.pd.click_remove_button()
 #     # sleep(2)
 #     # # self.pd.check_cart_count()
 #     # self.pd.hamburger_menu()
 #     # sleep(1)
 #     # self.pd.check_hamburger_menu_options()
