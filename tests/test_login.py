import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import PASSWORD, LOGIN
from url import URL

class TestLogIn:
    def test_login_from_main_page(self, driver):
        driver.get(URL.BASE)
        driver.find_element(*L.login_button_in_main_page).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход по кнопке «Войти в аккаунт» на главной'

    def test_login_from_main_page_acc(self, driver):
        driver.get(URL.BASE)
        driver.find_element(*L.acc_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку «Личный кабинет»'

    def test_login_from_register_page(self, driver):
        driver.get(URL.REGISTER)
        driver.find_element(*L.button_login_in_register).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку в форме регистрации'

    def test_login_from_forgot_password(self, driver):
        driver.get(URL.FORGOT_PASSWORD)
        driver.find_element(*L.button_login_in_register).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку в форме восстановления пароля'