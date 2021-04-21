from selenium.webdriver.common.by import By

from pageobjects.CheckOutPage import CheckOutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self , driver):
        self.driver = driver


    shopbtn = (By.CSS_SELECTOR ,"a[href*='shop']")
    name = (By.NAME ,"name")
    checkbox = (By.XPATH  , "//input[@id = 'exampleCheck1']")
    email = (By.CSS_SELECTOR , "input[name = 'email']")
    password = (By.CSS_SELECTOR , "input[id ='exampleInputPassword1']")
    #dob = (By.XPATH , "//input[@name ='bday']")
    dropdown = (By.ID , "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR , "input[class = 'btn btn-success']")
    def getshopbtn(self):
        self.driver.find_element(*HomePage.shopbtn).click()
        checkout = CheckOutPage(self.driver)
        return checkout
    def getname(self):
        return self.driver.find_element(*HomePage.name)
    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getemail(self):
        return self.driver.find_element(*HomePage.email)
    def getpassword(self):
        return self.driver.find_element(*HomePage.password)
    def getdob(self):
        wait = WebDriverWait(self.driver , 5)
        return wait.until(EC.presence_of_element_located((By.XPATH , "//input[@name ='bday']")))


    def getdropdown(self):
        return self.driver.find_element(*HomePage.dropdown)
    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)




