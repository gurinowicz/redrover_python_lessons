from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import *
from data import *
from faker import Faker


fake = Faker("ru_RU")


def test_order(browser, auth):
    # добавить товар в корзину
    browser.find_element(By.XPATH, t_shirt).click()
    time.sleep(3)
    # перейти в  корзину
    browser.find_element(By.CLASS_NAME, cart_icon).click()
    time.sleep(3)
    # переход на страницу оформления заказа
    browser.find_element(By.XPATH, checkout_button).click()
    # заполнение карточки заказа
    browser.find_element(By.ID, first_name_input).send_keys(fake.first_name())
    browser.find_element(By.ID, last_name_input).send_keys(fake.last_name())
    browser.find_element(By.ID, 'postal-code').send_keys(fake.postcode())
    browser.find_element(By.ID, continue_button).click()
    time.sleep(3)
    button = browser.find_element(By.XPATH, finish_button)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    element = browser.find_element(By.XPATH, '//*[text()="Thank you for your order!"]')
    element_message = element.text
    assert element_message == "Thank you for your order!", "error"