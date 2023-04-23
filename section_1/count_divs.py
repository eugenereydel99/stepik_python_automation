import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_count_divs():
    driver = webdriver.Chrome()

    driver.get(url="http://suninjuly.github.io/blog_example.html")

    time.sleep(5)

    divs = driver.find_element(By.TAG_NAME, "div")

    driver.quit()

    assert len(divs) == 7
