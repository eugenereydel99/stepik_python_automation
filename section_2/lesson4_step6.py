from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(time_to_wait=30)
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button").click()


finally:
    browser.quit()
