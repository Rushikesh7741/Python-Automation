import pytest
from selenium import webdriver
from time import sleep

from PageObjects.LoginPage import LoginPage
from PageObjects.Product import Product
from testCases.Conftest import setup
class Test_001_Login:
 baseURL="https://www.saucedemo.com/"
 username="standard_user"
 password="secret_sauce"
 def test(self, setup):
     self.driver =setup
     self.driver.get(self.baseURL)
     self.act_title=self.driver.title

 def test_Add_Product(self, setup):
    self.driver = setup

    self.driver.get(self.baseURL)
    sleep(1)

    self.driver.maximize_window()
    self.lp = LoginPage(self.driver)
    sleep(1)

    self.lp.setUserName(self.username)
    sleep(1)

    self.lp.setPassword(self.password)
    sleep(1)

    self.lp.clickLoginButton()
    sleep(1)

    self.pd = Product(self.driver)
    productName = 'sauce-labs-backpack'
    self.pd.add_product_click(productName)
    self.pd.verify_count(1)
    sleep(1)

    self.pd.shopping_cart()
    sleep(1)
    ProductName1="Sauce Labs Backpack"
    productsList=self.pd.get_product_list_from_cart()
    assert ProductName1 in productsList, "error msg"
    sleep(1)

    # self.pd.click_remove_button()
    # sleep(1)
    self.pd.click_on_continue_shopping_button()
    sleep(1)

    productName = "sauce-labs-bike-light"
    self.pd.add_product_click(productName)
    self.pd.verify_count(2)
    sleep(1)

    self.pd.shopping_cart()
    sleep(2)
    # self.pd.verify_products()
    # sleep(2)
    # self.pd.get_product_list_from_cart()
    ProductName1='Sauce Labs Bike Light'
    productsList = self.pd.get_product_list_from_cart()
    assert ProductName1 in productsList, "error msg"
    sleep(1)
    self.pd.click_remove_button()
    sleep(1)

    self.pd.click_on_continue_shopping_button()
    sleep(1)

    self.pd.click_on_hamburger_menu()
    sleep(1)
    HambuegerEle=['ALL ITEMS','ABOUT','LOGOUT','RESET APP STATE']
    HamBUrgerElements=self.pd.get_all_elements_of_hambeurger_menu()
    assert HambuegerEle == HamBUrgerElements ,"Elements are not matching"
    sleep(1)

    self.pd.click_on_close_button()
    sleep(1)

    self.pd.click_on_filter()
    sleep(2)

    self.pd.apply_filter(1)
    sleep(2)

    PL=['Sauce Labs Fleece Jacket','Sauce Labs Backpack','Sauce Labs Bolt T-Shirt','Test.allTheThings() T-Shirt (Red)','Sauce Labs Bike Light','Sauce Labs Onesie']
    PL.sort()
    AllProducts = self.pd.collect_all_products_in_list()
    assert PL == AllProducts ,"error message"

    self.pd.click_on_filter()
    sleep(2)

    self.pd.apply_filter(2)
    sleep(2)
    PL.sort(reverse=True)
    AllProducts1=self.pd.collect_all_products_in_list()
    assert PL==AllProducts1 ,"error message"

    self.pd.click_on_hamburger_menu()
    sleep(1)

    self.pd.click_on_logout_button()
    sleep(2)

    act_title=self.driver.title
    exp_title="Swag Labs"
    assert act_title == exp_title ,"user didn't logged out"


    # #
