import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element(By.XPATH, "//input[@name=\"firstname\"]").send_keys("Eugene")
browser.find_element(By.XPATH, "//input[@name=\"lastname\"]").send_keys("Reydel")
browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("test@mail.ru")

proj_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(proj_dir, "test.txt")
browser.find_element(By.CSS_SELECTOR, "input[name=\"file\"]").send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

time.sleep(5)
browser.quit()
