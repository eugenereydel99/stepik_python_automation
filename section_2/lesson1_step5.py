import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id=\"input_value\"]")

    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "[id=\"answer\"]")
    answer.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
