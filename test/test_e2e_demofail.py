from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest
#@pytest.mark.usefixtures("setup")
from pageobjects.CheckOutPage import CheckOutPage
from pageobjects.ConfirmPage import ConfirmPage
from pageobjects.HomePage import HomePage
from utilities.BaseClass import Baseclass

class Testone(Baseclass):  #we don't have to explicitly write use fixtures as once we mentioned it in
    def test_e2e(self):
        log = self.getLogger()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()
        shopbtn = HomePage(self.driver) #object
        log.info("clicked on shop button from homepage")
        checkout = shopbtn.getshopbtn()

        i = -1

        Prodtitles = checkout.gettitles()
        log.info("Getting all the titles of products dispalyed on checkout page")
        #Prodtitles = self.driver.find_elements_by_css_selector("div.card-body a")
        for titles in Prodtitles:
            i = i + 1
            log.info(titles.text)
            if (titles.text == "Blackberry"):
                addbtn = checkout.getAddBtn()
                addbtn[i].click()

        checkout.getCheckOut().click()
        confirmpage = checkout.getfinalcheckout()
        confirmpage.getcountryfield().send_keys("ind")
        #to give explicit wait and choose "India" from dropdown
        self.verifylinkpresent("India") #wait and verify India is present in link test or not

        confirmpage.getdropdown().click()
        confirmpage.getcheckbox().click()
        confirmpage.getpurchase().click()
        successText = confirmpage.getalert().text
        #adding this intentionally fail the test to see screenshot of failure.
        #assert use for assertion
        #modified again ......
        assert "Success! Thansssssssssssk you!" in successText #test will fail because of assertion error.
        log.info("Successfully placed order............")
        self.driver.get_screenshot_as_file("screen.png")  # To get screenshots

