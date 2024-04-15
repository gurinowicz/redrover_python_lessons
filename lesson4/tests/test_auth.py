from lesson4.pages.auth_page import LoginPage
import time

url = 'https://victoretc.github.io/selenium_waits/'


def test_auth_positive(driver):
    page = LoginPage(driver, url)
    page.open()
    time.sleep(5)