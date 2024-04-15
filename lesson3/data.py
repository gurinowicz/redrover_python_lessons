from faker import Faker
fake = Faker()

url = 'https://victoretc.github.io/selenium_waits/'
title_text = 'Практика с ожиданиями в Selenium'
start_btn_text = 'Начать тестирование'

login = fake.email()
password = fake.postcode()

