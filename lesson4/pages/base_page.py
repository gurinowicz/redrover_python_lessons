from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __int__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
