import time
import pytest
from selenium import webdriver

@pytest.mark.usefixture("drivername")
class TestToolsQA():

    def test_toolsqaform(self,driverName):
        if driverName == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        elif driverName == "firefox":
            driver = webdriver.Chrome(executable_path="C:\\geckodriver.exe")
        elif driverName == "IE":
            driver = webdriver.Chrome(executable_path="C:\\IEDriverServer.exe")

        driver.get("https://demoqa.com/automation-practice-form")
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@id='firstName']").send_keys("Nikos")
        driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Varelas")
        radio_button = driver.find_elements_by_xpath("//*[@id='genterWrapper']/div[2]/div[1]/label")
        radio_button[0].click()
        driver.find_element_by_xpath("//input[@id='userNumber']").send_keys("6912345678")
        driver.execute_script("window.scrollBy(0,1000)")
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(2)
        submit_text = driver.find_element_by_xpath("//div[@id='example-modal-sizes-title-lg']").text
        driver.get_screenshot_as_file("Sheets/ToolsQA_form.png")
        assert submit_text == "Thanks for submitting the form"


    def test_toolsqabooks(self,driverName):
        if driverName == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        elif driverName == "firefox":
            driver = webdriver.Chrome(executable_path="C:\\geckodriver.exe")
        elif driverName == "IE":
            driver = webdriver.Chrome(executable_path="C:\\IEDriverServer.exe")

        driver.get("https://demoqa.com/login")
        driver.maximize_window()
        driver.find_element_by_xpath("//button[@id='newUser']").click()
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Nikos")
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Varelas")
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("NikosVarel")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("Nikos0!")
        driver.get_screenshot_as_file("Sheets/ToolsQA_books.png")