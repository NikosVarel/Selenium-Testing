# Selenium-Testing

**PROJECT UNDER CONSTRUCTION**

This is a **Selenium-Pytest** demo. In this project I apply tests in demo site https://demoqa.com by **ToolsQA.com**, in pages:
        /automation-practice-form and /login.<br/>
Tests setup is for **Chrome**, **Firefox** and **IE** browsers and the choice is done by terminal. **pytest -v -s --driverName=chrome**.<br/>
The inputs are static, but are about to be inserted dymamically.<br/>
The main taget is:
  * by the **assertion**, to compare the expected with the actual outcomes
  * create a **report** of test enviroment,test cases test pass/fail. Also give an automated screenshot file with the browser test result
  * deliver a **error-warning** level report.


**TEST ARCHITECTURE**

  * The **driver** pytest requests included in **conftest.py** file<br/>
  * All tests are included in **tests** package.<br/>
  * A **BaseClass** class place in order driver call and test plans, in BaseClass package.<br/>
  * Αfter the plan is ready, we call BaseClass in **test_main**. **!!!** In test_main we can call and another test plans if we want with other requests.<br/>
  * test_main is ready to be executed as pytest.

<!-- Diagram editor -->
