import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element(By.CSS_SELECTOR, "img[id=\"treasure\"]")

x = treasure.get_attribute("valuex")

y = calc(x)

browser.find_element(By.XPATH, "//input[@id=\"answer\"]").send_keys(y)
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.XPATH, "//button[@type=\"submit\"]").click()

time.sleep(15)
browser.quit()
