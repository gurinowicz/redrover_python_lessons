import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
