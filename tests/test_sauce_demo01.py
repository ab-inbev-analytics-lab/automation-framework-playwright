import json
from playwright.sync_api import sync_playwright
import time
import pyautogui
import pytest  # For pressing F11 at OS level

#json_file -> util -> access into test
with open("data/credentials.json", "r") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
@pytest.mark.azure_test_case_id(128285)
def test_sauce_tc_one(user_credentials):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(viewport=None)
        page = context.new_page()

        # Go to Sauce Demo
        page.goto("https://www.saucedemo.com/")

        # Wait a moment for the window to appear
        time.sleep(1)

        # Press F11 to enter fullscreen
        pyautogui.press("f11")

        # Login
        page.fill("#user-name", user_credentials["username"])
        page.fill("#password", user_credentials["password"])
        page.click("#login-button")

        # Save cookies + local storage
        context.storage_state(path="auth_state.json")

        browser.close()