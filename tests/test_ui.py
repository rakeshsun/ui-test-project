import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    # Initialize the Chrome browser
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after the test
    driver.quit()

def test_google_search(browser):
    # Open Google
    browser.get("https://www.google.com")
    # Find the search box and enter a query
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins")
    search_box.submit()
    # Verify the title contains the search term
    assert "Jenkins" in browser.title

def test_google_fail(browser):
    # This test will fail intentionally
    browser.get("https://www.google.com")
    assert "NonExistentText" in browser.title