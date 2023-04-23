import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(url=link)

    # ищем кнопку для вызова подтверждающего окна
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

    # принимаем подтверждение
    confirm_window = browser.switch_to.alert
    confirm_window.accept()

    # проходим капчу
    x_value: str = browser.find_element(By.XPATH, "//span[@class=\"nowrap\"][@id=\"input_value\"]").text
    y_value = calc(int(x_value))
    browser.find_element(By.CSS_SELECTOR, "input[id=\"answer\"]"). \
        send_keys(y_value)

    # отправляем результат
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()


finally:
    time.sleep(10)
    browser.quit()
