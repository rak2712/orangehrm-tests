import pytest
import os
from pages.login_page import LoginPage

BASE_URL = os.getenv("BASE_URL")

@pytest.mark.parametrize("username, password, expected", [
    (os.getenv("USER_NAME"), os.getenv("PASSWORD"), "dashboard"),           # ✅ Positive
    ("invalid_user", os.getenv("PASSWORD"), "Invalid credentials"),        # ❌ Negative
    (os.getenv("USERNAME"), "wrongpass", "Invalid credentials"),           # ❌ Negative
])
def test_login(driver, username, password, expected):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected == "dashboard":
        assert "/dashboard" in driver.current_url
    else:
        assert expected in login_page.get_error_message()
