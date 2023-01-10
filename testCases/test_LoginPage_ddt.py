import pytest
from selenium import webdriver
from Utilities import xlutil
import time

from  PageObjects.LoginPage import LoginPage
from Utilities.readproperties import readconfig
from testCases.Conftest import setup
class Test_002_DDT_Login():
    baseURL = readconfig.ApplicationURL()
    path = "/home/excellarate/Desktop/Pyhton Automation/Python-Automation/TestData/testdata.xlsx"
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = xlutil.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=xlutil.readData(self.path,'Sheet1',r,1)
            self.password = xlutil.readData(self.path, 'Sheet1', r, 2)
            self.exp = xlutil.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='pass':
                    self.lp.clickLogout();
                    lst_status.append("pass")
                elif self.exp=='fail':
                    self.lp.clickLogout();
                    lst_status.append("fail")

            elif act_title!=exp_title:
                if self.exp == 'pass':
                    lst_status.append("fail")
                elif self.exp == 'fail':
                    lst_status.append("pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

