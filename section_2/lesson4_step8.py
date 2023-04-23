import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url="http://suninjuly.github.io/explicit_wait2.html")

    price_text = WebDriverWait(driver=browser, timeout=12).until(
        ec.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id=\"price\"]"), "$100")
    )

    book_btn = WebDriverWait(driver=browser, timeout=5).until(
        ec.element_to_be_clickable((By.ID, "book"))
    )
    book_btn.click()

    x_value = browser.find_element(By.ID, "input_value").text
    y_value = calc(int(x_value))

    browser.find_element(By.ID, "answer").send_keys(y_value)
    browser.find_element(By.XPATH, "//button[@type=\"submit\"]").click()

finally:
    time.sleep(10)
    browser.quit()
