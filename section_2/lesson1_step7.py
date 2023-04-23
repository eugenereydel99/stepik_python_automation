from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.is_enabled()
print(f"value of people radio: {people_checked}")
assert people_checked == True, "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print(f"value of robots radio: {robots_checked}")

browser.quit()
