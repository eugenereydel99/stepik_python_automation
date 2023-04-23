import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(url=link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Eugene")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Reydel")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Tomsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(
        By.XPATH,
        "//form//button[@type=\"submit\"][text()=\"Submit\"]"
    )

    if button.is_enabled():
        button.click()

finally:
    time.sleep(15)
    browser.quit()
