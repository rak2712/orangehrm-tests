from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        username_field = wait.until(EC.presence_of_element_located(self.username_input))
        password_field = wait.until(EC.presence_of_element_located(self.password_input))
        login_btn = wait.until(EC.element_to_be_clickable(self.login_button))

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_btn.click()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.presence_of_element_located(self.error_message)).text
