import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from faker import Faker
from lesson3.data import *
from lesson3.locators_3 import *


url = 'https://victoretc.github.io/selenium_waits/'
fake = Faker("ru_RU")


### Pre conditions : open website in Chromebrowser ###


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.quit()


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=30)
    return wait


def test_open_page(browser, wait):
    browser.get(url)
    title = browser.find_element(*title_text)
    assert title.text == "Практика с ожиданиями в Selenium", "error"
    start_test_btn = wait.until(EC.element_to_be_clickable(start_button))
    start_test_btn.click()
    assert start_test_btn.text == start_btn_text, 'you might have been lost if you are here'
    browser.find_element(*login_input).send_keys(login)
    browser.find_element(*password_input).send_keys(password)
    browser.find_element(*check_box).click()
    submit_btn = browser.find_element(*register_button)
    submit_btn.click()
    load_element = wait.until(EC.visibility_of_element_located(loader))
    assert load_element.is_displayed()
    success_msg = wait.until(EC.visibility_of_element_located(success_message))
    assert success_msg.text == "Вы успешно зарегистрированы!", "error"


def test_open_page_using_implicitly_wait(browser):
    browser.implicitly_wait(10)
    browser.get(url)
    start_test_btn = browser.find_element(*start_button)
    start_test_btn.click()
    assert start_test_btn.is_displayed()
    browser.find_element(*login_input).send_keys(login)
    browser.find_element(*password_input).send_keys(password)
    browser.find_element(*check_box).click()
    submit_btn = browser.find_element(*register_button)
    submit_btn.click()
    load_element = browser.find_element(*loader)
    assert load_element.is_displayed()
    time.sleep(5)
    assert browser.find_element(*success_message).is_displayed()
    success_msg = browser.find_element(*success_message).get_attribute('id')
    assert success_msg == 'successMessage', "что-то не то"


def test_open_page_using_time_sleep(browser):
    browser.get(url)
    time.sleep(5)
    start_test_btn = browser.find_element(*start_button)
    start_test_btn.click()
    time.sleep(10)
    assert start_test_btn.is_displayed()

    browser.find_element(*login_input).send_keys(login)
    browser.find_element(*password_input).send_keys(password)
    browser.find_element(*check_box).click()

    submit_btn = browser.find_element(*register_button)
    submit_btn.click()

    load_element = browser.find_element(*loader)
    assert load_element.is_displayed()
    time.sleep(5)

    assert browser.find_element(*success_message).is_displayed()
    success_msg = browser.find_element(*success_message).get_attribute('id')
    assert success_msg == 'successMessage', "что-то не то"