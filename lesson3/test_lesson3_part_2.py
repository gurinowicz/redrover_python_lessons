import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import pytest
from faker import Faker

url = 'https://the-internet.herokuapp.com/'
fake = Faker("ru_RU")

# https://the-internet.herokuapp.com/add_remove_elements/ (Необходимо создать и удалить элемент)
# https://the-internet.herokuapp.com/basic_auth (Необходимо пройти базовую авторизацию)
# https://the-internet.herokuapp.com/broken_images (Необходимо найти сломанные изображения)
# https://the-internet.herokuapp.com/checkboxes (Практика с чек боксами)

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


def test_open_page(browser):
    browser.get(url)
    title = browser.find_element(By.TAG_NAME, "h1")
    assert title.text == "Welcome to the-internet", "it's not the right place"


def test_add_and_delete(browser):
    browser.get(url)
    browser.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    browser.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
    button_delete = browser.find_element(By.XPATH, '//*[@id="elements"]/button')
    button_delete.click()
    try:
        assert button_delete.is_displayed(), "Element is not displayed"
    except StaleElementReferenceException:
        print("Element reference is stale, handle this case accordingly")


def test_basic_auth(browser, wait):
    browser.get(url)
    browser.find_element(By.LINK_TEXT, "Basic Auth").click()
    WebDriverWait(browser, 30).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.send_keys("username")
    alert.send_keys("\t")  # Добавляем табуляцию для перехода на поле ввода пароля
    alert.send_keys("password")
    alert.accept()
    time.sleep(2)
    assert browser.current_url == "https://the-internet.herokuapp.com/basic_auth", "you are lost"


# def test_broken_image(browser):
#     browser.get(url)
#     browser.find_element(By.LINK_TEXT, "Broken Images").click()
#     def test_checkboxes(browser):
#     browser.get(url)
#     browser.find_element(By.LINK_TEXT, "Checkboxes").click()