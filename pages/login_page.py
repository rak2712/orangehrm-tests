from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text
