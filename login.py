from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Open new page
    page = browser.new_page()

    # Open website
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter username
    page.locator('input[name="username"]').fill("Admin")

    # Enter password
    page.locator('input[name="password"]').fill("admin123")

    # Click login button
    page.locator('button[type="submit"]').click()

    # Wait for dashboard page
    page.wait_for_url("**/dashboard/index")

    # Validation
    expect(page.locator("h6")).to_have_text("Dashboard")

    print("Login Successful")

    # Close browser
    browser.close()