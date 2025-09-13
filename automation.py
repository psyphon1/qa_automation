import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

def test_login_add_to_cart_and_verify_count(page: Page):

    #Test script to verify that a user can log in,) test script to verify that a user can log in,
    
    page.goto("https://www.saucedemo.com/")
    print("Navigated to Sauce Demo login page.")

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    
    page.locator("[data-test=\"login-button\"]").click()
    print("Logged in with standard_user.")

    expect(page).to_have_url(re.compile(r".*inventory\.html"))
    print("Login successful, redirected to inventory page.")

    backpack_item = page.locator(".inventory_item", has_text="Sauce Labs Backpack")
    backpack_item.get_by_role("button", name="Add to cart").click()
    print("Added 'Sauce Labs Backpack' to the cart.")

    cart_badge = page.locator(".shopping_cart_badge")
    
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("1")
    print("Successfully verified that the cart count is 1.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        test_login_add_to_cart_and_verify_count(page)
        
        page.wait_for_timeout(3500) 
        
        browser.close()

