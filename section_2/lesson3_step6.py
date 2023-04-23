import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"].trollface.btn").click()
    first_window = browser.current_window_handle

    # переходим на новую вкладку
    redirect_window = browser.window_handles[1]
    browser.switch_to.window(window_name=redirect_window)

    x_value = browser.find_element(By.ID, "input_value").text
    y_value = calc(int(x_value))

    browser.find_element(By.ID, "answer").send_keys(y_value)
    browser.find_element(By.XPATH, "//button[@type=\"submit\"]").click()

finally:
    time.sleep(5)
    browser.quit()
