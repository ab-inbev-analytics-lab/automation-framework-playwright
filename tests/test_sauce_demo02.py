from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # Load saved state
    context = browser.new_context(storage_state="auth_state.json")
    page = context.new_page()

    # Go directly to a logged-in page
    page.goto("https://www.saucedemo.com/inventory.html")

    page.wait_for_timeout(3000)  # Just to see the page
    browser.close()