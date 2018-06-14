import pytest
import unittest
from baseUtils.invoke_browser import InvokeBrowser
from selenium import webdriver
import os

@pytest.fixture()
def setUp():
    print("this will run before every test")
    yield
    print("this will run after everytest")

@pytest.fixture(scope="class")
def oneTimeSetUp(request,browser):
    # driver=None
    # if browser=="chrome":
    #     workingDir = os.path.dirname(__file__)
    #     driverDir = "../drivers/"
    #     chromeEXe = driverDir + "chromedriver.exe"
    #     driverLocation = os.path.join(workingDir, chromeEXe)
    #     print(driverLocation)
    #     driver = webdriver.Chrome(driverLocation)
    # driver.get("http://demoqa.com/registration/")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    driver=InvokeBrowser().opneBrowser(browser)
    print("this will run once before the test")
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    driver.quit()
    print("this will run once after the test")


def pytest_addoption(parser):
    # parser.addoption("--browser",action="store", default="chrome", help="Type in browser type")
    parser.addoption("--browser")
    parser.addoption("--osType",help="here we will get the osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--osType")