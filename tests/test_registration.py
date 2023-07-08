import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from url import URL

class TestRegistration:
    def test_register_new_user(self, driver):
        driver.get(URL.REGISTER)
        driver.find_element(*L.register_name).send_keys('vlad')
        driver.find_element(*L.login_email).send_keys(str(randint(000000, 999999)) + '@.com')
        driver.find_element(*L.register_password).send_keys('123456789')
        driver.find_element(*L.register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        assert driver.current_url == URL.LOGIN_PAGE
        # Хоть убей не пойму, почему не переходит. Уже перепробовал все WebDriverWait, но думаю проблема не в нем

    def test_register_unvalid(self, driver):
        driver.get(URL.REGISTER)
        driver.find_element(*L.register_name).send_keys('vlad')
        driver.find_element(*L.login_email).send_keys(str(randint(000000, 999999)) + '@yandex.ru')
        driver.find_element(*L.register_password).send_keys('123')
        driver.find_element(*L.register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.text_error_register))
        error_text = driver.find_element(*L.text_error_register).text
        assert error_text == 'Некорректный пароль', 'Некорректный пароль'