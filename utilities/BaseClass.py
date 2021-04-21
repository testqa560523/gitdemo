import inspect

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
import logging

@pytest.mark.usefixtures("setup")
class Baseclass:

    def verifylinkpresent(self , text):   #generic verifylinktext method
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionInDropDown(self ,locator, text):
        dropdown = Select(locator.getdropdown())  # for capturing all the options of dropdowns
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]  #get method name from where this method is called.
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


