import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginPage:
    '''This class has all the locators and action methods for the elements of the Homepage only'''

    def __init__(self):
        self.login_button = "login-menu"
        self.username_field = "j_username"
        self.password_field = "j_password"
        self.go_button = "//button[contains(text(), 'Go')]"
        self.error_message = "//form[@id='command']//p"

    def click_login_button(self, driver):
        driver.find_element(By.ID, self.login_button).click()

    def enter_username(self, driver, username):
        driver.find_element(By.ID, self.username_field).send_keys(username)

    def enter_password(self, driver, password):
        driver.find_element(By.ID, self.password_field).send_keys(password)

    def click_go_button(self, driver):
        driver.find_element(By.XPATH, self.go_button).click()

    def get_error_message(self, driver):
        return driver.find_element(By.XPATH, self.error_message).text
