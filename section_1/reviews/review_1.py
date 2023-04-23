import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "firstname")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
input4.send_keys("Russia")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
browser.quit()
