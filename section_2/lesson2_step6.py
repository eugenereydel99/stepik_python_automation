import math
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(url="https://SunInJuly.github.io/execute_script.html")

x_element = browser.find_element(By.ID, "input_value").text
y_element = calc(int(x_element))

# browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
browser.execute_script("document.querySelector('footer').remove()")

browser.find_element(By.XPATH, "//input[@id=\"answer\"]").send_keys(y_element)
browser.find_element(By.XPATH, "//input[@id=\"robotCheckbox\"]").click()
browser.find_element(By.XPATH, "//input[@id=\"robotsRule\"][@type=\"radio\"]").click()
browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

time.sleep(15)
browser.quit()
