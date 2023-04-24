import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistrationForm(unittest.TestCase):
    def test_registration1_form(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        firstname = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .first"
        )
        firstname.send_keys("Eugene")

        lastname = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .second"
        )
        lastname.send_keys("Schneider")

        email = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .third"
        )
        email.send_keys("test@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2_form(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        firstname = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .first"
        )
        firstname.send_keys("Eugene")

        lastname = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .second"
        )
        lastname.send_keys("Schneider")

        email = browser.find_element(
            By.CSS_SELECTOR,
            ".first_block .third"
        )
        email.send_keys("test@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    unittest.main()
