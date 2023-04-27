import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service('../chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser...")
    browser.quit()
