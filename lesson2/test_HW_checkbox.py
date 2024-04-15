import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson1.data import *
from locators import *


def test_checkbox(browser):
    browser.get('https://victoretc.github.io/webelements_information/')
    browser.find_element(By.ID, "username").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "agreement").click()
    assert browser.find_element(By.ID, "registerButton").is_enabled()


def test_checkbox_without_user_name(browser):
    browser.get('https://victoretc.github.io/webelements_information/')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "agreement").click()
    assert browser.find_element(By.ID, "registerButton").get_attribute('disabled')


def test_checkbox_without_password(browser):
    browser.get('https://victoretc.github.io/webelements_information/')
    browser.find_element(By.ID, "username").send_keys('standard_user')
    browser.find_element(By.ID, "agreement").click()
    assert browser.find_element(By.ID, "registerButton").get_attribute('disabled')


def test_checkbox_without_agreement(browser):
    browser.get('https://victoretc.github.io/webelements_information/')
    browser.find_element(By.ID, "username").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    assert browser.find_element(By.ID, "registerButton").get_attribute('disabled')