from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

dropdown_list = Select(browser.find_element(By.CSS_SELECTOR, "[id='dropdown']"))
# options = browser.find_elements(By.CSS_SELECTOR, "select[id='dropdown'] option")
#
# for index, option in enumerate(options):
#     print(f"{index}: {option.get_attribute('value')}")

dropdown_list.select_by_value("1")

browser.quit()
