import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import *
from data import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from faker import Faker
from selenium.webdriver.support.select import Select


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def auth(browser):
    browser.get(URL)
    browser.find_element('xpath', USER_NAME_FIELD).send_keys(VALID_LOGIN)
    browser.find_element(By.XPATH, USER_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    browser.find_element(By.XPATH, LOGIN_BUTTON).click()
    return auth


@pytest.fixture()
def auth_invalid_name(browser):
    browser.get(URL)
    browser.find_element('xpath', USER_NAME_FIELD).send_keys(INVALID_LOGIN)
    browser.find_element(By.XPATH, USER_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    browser.find_element(By.XPATH, LOGIN_BUTTON).click()
    return auth_invalid_name


@pytest.fixture()
def faker_login(browser):
    fake = Faker()
    login = fake.user_name()
    return {'login': login}


@pytest.fixture()
def purchases(browser, auth):
    browser.find_element(By.ID, 'item_2_title_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed()
    yield
    return purchases
#     browser.find_element(By.ID, 'remove').click()
#     return add_item_to_cart


@pytest.fixture()
def open_dropdown_menu(browser,auth):
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()
    select = Select(dropdown)
    select.select_by_index(1)
    yield
    return open_dropdown_menu


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver


@pytest.mark.parametrize("item_index", range(1, 13))
def test_add_item_to_cart(browser, auth, item_index):
    browser.find_element(By.CLASS_NAME, f"(ITEM)[{item_index}]").click()
    browser.find_element(By.ID, BUTTON_ADD).click()
    assert browser.find_element(By.CLASS_NAME, CART_BADGE_LOCATOR).is_displayed()
    # remove_button = browser.find_element(By.ID, 'remove')
    # remove_button.click()