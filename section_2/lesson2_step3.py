import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

left_value = browser.find_element(By.ID, "num1").text
print(left_value)
right_value = browser.find_element(By.ID, "num2").text
print(right_value)
result = int(left_value) + int(right_value)
print(result)

browser.implicitly_wait()

dropdown_list = Select(browser.find_element(By.CSS_SELECTOR, "select[id='dropdown']"))
dropdown_list.select_by_value(str(result))

browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(15)
browser.quit()
