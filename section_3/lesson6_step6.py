from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

browser = webdriver.Firefox()
browser.get("https://stepik.org/lesson/25969/step/8")
