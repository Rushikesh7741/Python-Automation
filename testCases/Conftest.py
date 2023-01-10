
from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

########## Pytest HTML Report ###################
def pytest_configure(config):
    config.metadata['project name'] ='nop commerce'
    config.metadata['Module Name'] ='Customers'
    config.metadata['Tester']='Hrishikesh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA-HOME",None)
    metadata.pop("Plugins",None)

    def pytest_addoption(parser):
        parser.addoption("--browser-version")

    def pytest_html_report_title(report):
        report.title = "need browser version string here"