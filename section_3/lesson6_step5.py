import math
import time

import pytest
import selenium.webdriver.support.expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    service = Service('../chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.quit()


@pytest.fixture
def credentials():
    return "", ""


@pytest.mark.parametrize(
    "link", [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]
)
class TestForm:

    def test_authorization_correct(self, browser, link, credentials):
        browser.get(url=link)
        browser.delete_all_cookies()

        WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.ID, "ember33"))
        ).click()

        browser.find_element(By.ID, "id_login_email").send_keys(credentials[0])
        browser.find_element(By.ID, "id_login_password").send_keys(credentials[1])
        browser.find_element(By.CSS_SELECTOR, "button[class=\"sign-form__btn button_with-loader \"]").click()

        text_area = WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        text_area.clear()
        text_area.send_keys(str(math.log(int(time.time()))))

        WebDriverWait(driver=browser, timeout=15).until_not(
            ec.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        ).click()

        smart_hint = WebDriverWait(browser, 15).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".attempt__message p"))
        ).text

        result = smart_hint
        print(result)

        assert result == "Correct!", \
            f"Expected smart_hint should be equal 'Correct!', but equal {result}"
