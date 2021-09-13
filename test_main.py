import time
from selenium import webdriver

def test_toolsqa(driverName):
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
    assert submit_text == "Thanks for submitting the form"