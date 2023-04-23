import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def get_url():
    return "https://suninjuly.github.io/text_input_task.html"


def test_first_script(get_url):
    driver = webdriver.Chrome()

    time.sleep(5)  # делаем задержку для того, чтобы увидеть происходящее в браузере

    # через драйвер запускаем указанный сайт
    driver.get(get_url)
    time.sleep(5)

    textarea = driver.find_element(by=By.CSS_SELECTOR, value=".textarea")
    textarea.send_keys("get()")
    time.sleep(5)

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".submit-submission")
    submit_button.click()
    time.sleep(5)

    driver.quit()
