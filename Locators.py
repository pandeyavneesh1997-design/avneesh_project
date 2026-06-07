from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Open Login Page
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Login
page.locator('input[name="username"]').fill("Admin")
page.locator('input[name="password"]').fill("admin123")
page.locator('button[type="submit"]').click()
page.wait_for_url(3000)
expect()
browser.close()
