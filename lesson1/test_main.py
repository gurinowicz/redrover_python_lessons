import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import *


def test_auth_positive(browser, auth):
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'


def test_auth_negative(browser, auth_invalid_name):
    assert browser.find_element(By.CSS_SELECTOR, LOGIN_ERROR).is_displayed(), "smth went wrong"


def test_add_item_positive(browser, auth):
    browser.find_element(By.XPATH, ADD_BIKE_ITEM).click()
    assert browser.find_element(By.CLASS_NAME, CART_BADGE_LOCATOR).is_displayed()


def test_remove_from_cart(browser, auth):
    browser.find_element(By.XPATH, ADD_BIKE_ITEM).click()
    browser.find_element(By.CLASS_NAME, CART_LINK).click()
    browser.find_element(By.ID, REMOVE_BIKE_FROM_THE_CART).click()
    assert browser.find_element(By.CLASS_NAME, REMOVED_ITEM).is_enabled()


def test_add_item_from_the_card(browser, auth):
    browser.find_element(By.ID, ADD_ITEM_4).click()
    browser.find_element(By.ID, BUTTON_ADD).click()
    assert browser.find_element(By.CLASS_NAME, CART_BADGE_LOCATOR).is_displayed()


def test_remove_item_from_the_card(browser, auth):
    browser.find_element(By.ID, ADD_ITEM_4).click()
    browser.find_element(By.ID, BUTTON_ADD).click()
    assert browser.find_element(By.CLASS_NAME, CART_BADGE_LOCATOR).is_displayed()
    time.sleep(3)
    browser.find_element(By.ID, REMOVE).click()
    assert browser.find_element(By.ID, BUTTON_ADD).is_enabled(), "Item was not removed from the cart from the item page"


# # Карточка товара
# # Успешный переход к карточке товара после клика на картинку товара
def test_open_item_from_the_picture(browser, auth):
    title_id = 5
    browser.find_element(By.ID, f'item_{title_id}_title_link').click()
    assert browser.current_url == f'https://www.saucedemo.com/inventory-item.html?id={title_id}'


def test_successful_open_product_card(browser, auth):
    item_id = 5
    browser.find_element(By.ID, f'item_{item_id}_img_link').click()
    assert browser.current_url == f'https://www.saucedemo.com/inventory-item.html?id={item_id}'


# # Оформление заказа
# # Оформление заказа используя корректные данные
#
def test_order_purchase_using_correct_datas(browser, auth, purchases):
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    browser.find_element(By.ID, 'checkout').click()
    browser.find_element(By.ID, 'first-name').send_keys('yana')
    browser.find_element(By.ID, 'last-name').send_keys('hur')
    browser.find_element(By.ID, 'postal-code').send_keys('222827')
    browser.find_element(By.ID, 'continue').click()
    browser.find_element(By.ID, 'finish').click()
    assert 'Thank you for your order!' in browser.page_source, "Text 'Thank you for your order!' not found on the page"


# # Фильтр
# # Проверка работоспособности фильтра (A to Z)



def test_filter_a_z(browser, auth, open_dropdown_menu):
    products = browser.find_elements(By.CLASS_NAME, FIND_PRODUCTS_IN_DD)
    product_names = [product.text for product in products]
    sorted_product_names = sorted(product_names)
    assert product_names == sorted_product_names, 'что-то не то'

# Проверка работоспособности фильтра (Z to A)


def test_filter_z_a(browser, auth, open_dropdown_menu):
    products = browser.find_elements(By.CLASS_NAME, FIND_PRODUCTS_IN_DD)
    product_names = [product.text for product in products]
    sorted_product_names = sorted(product_names, reverse=True)
    assert product_names == sorted_product_names, 'что-то не то'


def test_filter_low_to_high(browser, auth):
    Select(browser.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value('lohi')
    time.sleep(3)
    prices = browser.find_elements(By.CLASS_NAME, FIND_PRICES_IN_DD)
    price_names = [float(price.text[1::]) for price in prices]
    sorted_product_prices = sorted(price_names)
    assert price_names == sorted_product_prices, 'Ошибка: Цены не отсортированы по возрастанию'


# Проверка работоспособности фильтра (high to low)
def test_filter_high_to_low(browser, auth, open_dropdown_menu):
    prices = browser.find_elements(By.CLASS_NAME, FIND_PRICES_IN_DD)
    sorted_prices = [float(price.text.replace('$','')) for price in prices]
    assert sorted(sorted_prices, reverse=True) == [49.99, 29.99, 15.99, 15.99, 9.99, 7.99], 'Ошибка: Цены не отсортированы по убыванию'

#
# # Бургер меню
# # Выход из системы


def test_burger_login_out(browser):
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    browser.find_element(By.CSS_SELECTOR, '#login-button').click()
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/', 'smth goes wrong'

    browser.quit()
#
#
# # Проверка работоспособности кнопки "About" в меню
# def test_about_is_exist(browser):
#     browser.get('https://www.saucedemo.com/')
#     browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
#     browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
#     browser.find_element(By.CSS_SELECTOR, '#login-button').click()
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(2)
#     browser.find_element(By.ID, 'about_sidebar_link').click()
#     assert browser.current_url == 'https://saucelabs.com/', 'unreal link'
#     assert browser.find_element(By.CSS_SELECTOR,'[src="/images/logo.svg"]').is_displayed(), "Логотип отсутствует на главной странице"
#
#     browser.quit()
#
#
# def test_click_about(browser):
#     browser.maximize_window()
#     # browser.set_window_size(300, 500)
#     browser.get("https://www.saucedemo.com/")
#     browser.find_element('css selector', '#user-name').send_keys('standard_user')
#     browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
#     browser.find_element(By.CSS_SELECTOR, '#login-button').click()
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(3)
#     browser.find_element(By.ID, 'about_sidebar_link').click()
#     assert browser.current_url == 'https://saucelabs.com/'
#     time.sleep(5)
#     assert browser.find_element(By.CSS_SELECTOR, '[src="/images/logo.svg"]').is_displayed()
#     browser.quit()
#
#
# # Проверка работоспособности кнопки "Reset App State"
# def test_reset_is_work(browser):
#     browser.get('https://www.saucedemo.com/')
#     browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
#     browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
#     browser.find_element(By.CSS_SELECTOR, '#login-button').click()
#     browser.find_element(By.ID, 'item_4_img_link').click()
#     browser.find_element(By.ID, 'add-to-cart').click()
#     time.sleep(2)
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(2)
#     browser.find_element(By.ID, 'reset_sidebar_link').click()
#     assert 'shopping_cart_badge' not in browser.page_source, 'Ошибка: значок корзины присутствует'
#
#     browser.quit()
#
#
# def test_click_on_reset(browser):
#     browser.get('https://www.saucedemo.com/')
#     browser.find_element('css selector', '#user-name').send_keys('standard_user')
#     browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
#     browser.find_element(By.CSS_SELECTOR, '#login-button').click()
#
#     browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
#     assert 'shopping_cart_badge' in browser.page_source
#     browser.find_element(By.ID, 'react-burger-menu-btn').click()
#     WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.ID, 'reset_sidebar_link'))).click()
#     assert 'shopping_cart_badge' not in browser.page_source
#
#     browser.quit()
#
#
#
#
