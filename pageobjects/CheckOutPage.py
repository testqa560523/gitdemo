from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self , driver):
        self.driver = driver


    product_titles = (By.CSS_SELECTOR ,"div.card-body a")
    Add_btn = (By.CSS_SELECTOR , ".card-footer button")
    checkout = (By.CSS_SELECTOR , "a[class*='btn-primary']")
    finalcheckout = (By.XPATH , "//button[@class = 'btn btn-success']")
    def gettitles(self):
        return self.driver.find_elements(*CheckOutPage.product_titles)

    def getAddBtn(self):
        return  self.driver.find_elements(*CheckOutPage.Add_btn)

    def getCheckOut(self):
        return  self.driver.find_element(*CheckOutPage.checkout)

    def getfinalcheckout(self):
        self.driver.find_element(*CheckOutPage.finalcheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage


