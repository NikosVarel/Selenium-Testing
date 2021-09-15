class UnitTestBooks:
    def test_toolsqabooks(self):

        self.driver.get("https://demoqa.com/login")
        self.driver.maximize_window()

        self.driver.find_element_by_xpath("//button[@id='newUser']").click()
        self.driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Nikos")
        self.driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Varelas")
        self.driver.find_element_by_xpath("//input[@id='userName']").send_keys("NikosVarel")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Nikos0!")
        self.driver.get_screenshot_as_file("Sheets/ToolsQA_books.png")