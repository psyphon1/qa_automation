Sauce Demo - E2E Cart Verification Test
This project contains an automated end-to-end test script for the Sauce Demo website, written in Python using the Playwright framework.

The script simulates a complete user journey: logging in, adding an item to the shopping cart, and verifying that the cart updates correctly. This serves as a basic smoke test to ensure core e-commerce functionality is working as expected.

🚀 Features
Login: Automates user login with valid credentials.

Add to Cart: Selects a specific product ("Sauce Labs Backpack") and adds it to the cart.

Cart Verification: Asserts that the shopping cart's item counter accurately reflects the addition.

Visual Execution: Runs in "headed" mode by default, so you can watch the test execute in a live browser window.

📋 Prerequisites
Before you can run this script, you will need the following installed on your system:

Python (version 3.8 or newer)

pip (Python's package installer)

⚙️ Setup and Installation
Follow these steps to set up your environment:

Clone or Download the Script:
Save the test_saucedemo.py file to a local directory on your computer.

Install Playwright:
Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command to install the Playwright library:

pip install playwright

Install Browser Binaries:
Playwright needs browser binaries to run the tests. Install them with this simple command:

playwright install

This will download the necessary browser executables for Chromium, Firefox, and WebKit.

▶️ How to Run the Test
With the setup complete, you can execute the test script:

Navigate to the script's directory in your terminal.

Run the script using the following command:

python test_saucedemo.py

A new Chromium browser window will open and automatically perform the test steps. The script will print its progress to the terminal, confirming each major action.

🔧 Customization
Run Headless: To run the test in the background without a visible browser window, open test_saucedemo.py and change line 43 from headless=False to headless=True.

Change Browser: To use a different browser, change p.chromium.launch to p.firefox.launch or p.webkit.launch.