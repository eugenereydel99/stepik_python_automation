from selenium import webdriver

from selenium.webdriver.common.by import By


def test_locator():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        button = browser.find_element(By.ID, "submit_button")
        button.click()

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
