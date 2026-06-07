from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Xpath - Relative xpath  '//'
    # using attribute -   //tagname[@attributename = "value"]

    # page.locator('//input[@name="username"]').fill("Admin")
    # page.locator('//input[@placeholder="Password"]').fill("admin123")
    # page.locator('//button[@type="submit"]').click()
  # Wait for dashboard page
  #   page.wait_for_url("**/dashboard/index")
    # # Validation
    # expect(page.locator("h6")).to_have_text("Dashboard")
    # print("Login Successful")

# # text -  //tagname[text()="text"]
#     page.locator('//p[text()="Forgot your password? "]').click()
#     page.wait_for_timeout(2000)
#     browser.close()

#Contains
# attributes -  //tagname[contains(@attribute, "value")]

#Dynamic -  avneesh123, avneesh13456,avneesh789
# starts with -  //tagname[starts-with(id,'avneesh')]
# ends with -  2345user

# Family
# parent - //tagname[@id = "xy"]/ parent::input[]
# child -  //tagname[@id = "xy"]/ child::input[]
# ancestor - //td[text() = "Microsoft"]//following-sibling::td[2]