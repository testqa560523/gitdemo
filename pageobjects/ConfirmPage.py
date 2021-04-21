from selenium.webdriver.common.by import By
class ConfirmPage:
    def __init__(self , driver):
        self.driver = driver
    country = (By.ID , "country")
    Indiadropdown = (By.LINK_TEXT , "India")
    checkbox =(By.XPATH , "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR , "[type='submit']")
    alerttext = (By.CLASS_NAME , "alert-success")
    def getcountryfield(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getdropdown(self):
        return self.driver.find_element(*ConfirmPage.Indiadropdown)

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getpurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getalert(self):
        return self.driver.find_element(*ConfirmPage.alerttext)
