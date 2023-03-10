import pytest
from selenium import webdriver

from  PageObjects.LoginPage import LoginPage
from testCases.Conftest import setup
class Test_001_Login:
 baseURL="https://admin-demo.nopcommerce.com/"
 username="admin@yourstore.com"
 password="admin"
 def test(self, setup):
     self.driver =setup
     self.driver.get(self.baseURL)
     act_title=self.driver.title

     if act_title== "Your store. Login" :
         assert True
         self.driver.close()
     else:
         self.driver.save_screenshot(".//Screenshots//"+"test.png")
         self.driver.close()
         assert False


 def test_login(self,setup):
     self.driver=setup
     self.driver.get(self.baseURL)
     self.lp=LoginPage(self.driver)
     self.lp.setUserName(self.username)
     self.lp.setPassword(self.password)
     self.lp.clickLoginButton()
     act_title=self.driver.title
     if act_title=="Dashboard / nopCommerce administration":

         assert  True
         self.driver.close()
     else:
         self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
         self.driver.close()
         assert False


