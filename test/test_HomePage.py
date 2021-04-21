from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select     #Use to select dropdowns
import pytest

from TestData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.BaseClass import Baseclass
import time
class TestHomePage(Baseclass):

    def test_formSubmission(self ,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getData["name"])  # capture elemement by name
        log.info(f"name is {getData['name']}")
        homepage.getcheckbox().click()  # capture element by xpath
        homepage.getemail().send_keys(getData["email"])
        log.info(f"email is {getData['email']}")
        homepage.getpassword().send_keys("Pet@12345")
        homepage.getdob().send_keys("26-05-1994")
        self.selectOptionInDropDown(homepage , getData["gender"])  #select male in dropdown(Generic)
        log.info(f"gender is {getData['gender']}")
        time.sleep(2)
        homepage.getsubmit().click()
        # Assertion on success alert after submission of form

        Success_text = self.driver.find_element_by_css_selector("[class *= alert-success]").text  # using css selector

        print("****************************************************************")
        print(Success_text)
        assert ("Success" in Success_text)  # Give error if "success is not present"
        log.info("Test case completed....successfully submitted form")
        self.driver.refresh()  #to remove previously loaded data to enter new data
        log.info("refreshing page.....")
    @pytest.fixture(params = HomePageData.TestPageData.gettestdata("Testcase1"))  #to load different data to the home page form.
    def getData(self , request):
        return request.param



