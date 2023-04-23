from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(time_to_wait=30)
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.find_element(By.CSS_SELECTOR, "button[id=\"verify\"]").click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
