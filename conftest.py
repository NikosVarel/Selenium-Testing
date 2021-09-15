import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--driverName", action="store", default="Chrome")

# @pytest.fixture(scope="class")
# def driverName(request):
#     return request.config.getoption("--driverName")

@pytest.fixture(scope="class")
def setup(request):
    driverName = request.config.getoption("--driverName")
    if driverName == "Chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif driverName == "Firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif driverName == "IE":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
    request.cls.driver = driver
    yield
    driver.close()

    # if driverName == "chrome":
#         driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#     elif driverName == "firefox":
#         driver = webdriver.Chrome(executable_path="C:\\geckodriver.exe")
#     elif driverName == "IE":
#         driver = webdriver.Chrome(executable_path="C:\\IEDriverServer.exe")