from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

s=Service('/Users/olesya/IdeaProjects/chromedriver/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true')
driver.set_window_size(1366, 768)
driver.find_element(By.ID, 'login-button').click()
driver.find_element(By.ID, 'login-otp-button').click()

try:
    driver.find_element(By.XPATH, '//div[@class="navbar-inner"]')
except NoSuchElementException:
    TestCase.fail("Панель вкладок не найдена")

try:
    driver.find_element(By.ID, 'logo')
except NoSuchElementException:
    TestCase.fail("Логотип не найден")

try:
    driver.find_element(By.XPATH, '//a[@id="user-avatar"]')
except NoSuchElementException:
    TestCase.fail("Аватар не найден")
time.sleep(5)
