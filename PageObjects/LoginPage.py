from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath="//input[@data-test='username']"
    textbox_password_xpath="//input[@name='password']"
    login_button_xpath="//input[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
