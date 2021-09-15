import time
import pytest

@pytest.mark.usefixtures("setup")
class TestToolsQA:

    def test_toolsqaform(self,setup):

        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()

        self.driver.find_element_by_xpath("//input[@id='firstName']").send_keys("Nikos")
        self.driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Varelas")
        radio_button = self.driver.find_elements_by_xpath("//*[@id='genterWrapper']/div[2]/div[1]/label")
        radio_button[0].click()
        self.driver.find_element_by_xpath("//input[@id='userNumber']").send_keys("6912345678")
        self.driver.execute_script("window.scrollBy(0,1000)")
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(2)
        submit_text = self.driver.find_element_by_xpath("//div[@id='example-modal-sizes-title-lg']").text
        self.driver.get_screenshot_as_file("Sheets/ToolsQA_form.png")
        assert submit_text == "Thanks for submitting the form"


    def test_toolsqabooks(self,setup):

        self.driver.get("https://demoqa.com/login")
        self.driver.maximize_window()

        self.driver.find_element_by_xpath("//button[@id='newUser']").click()
        self.driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Nikos")
        self.driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Varelas")
        self.driver.find_element_by_xpath("//input[@id='userName']").send_keys("NikosVarel")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Nikos0!")
        self.driver.get_screenshot_as_file("Sheets/ToolsQA_books.png")

