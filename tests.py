import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import BASE, REGISTER, LOGIN_PAGE, PASSWORD, LOGIN, FORGOT_PASSWORD, ACCOUNT_PROFILE, ACCOUNT
from random import randint

class TestRegistration:
    def test_register_new_user(self, driver):
        driver.get(REGISTER)
        driver.find_element(*L.register_name).send_keys('vlad')
        driver.find_element(*L.login_email).send_keys(str(randint(000000, 999999)) + '@.com')
        driver.find_element(*L.register_password).send_keys('123456789')
        driver.find_element(*L.register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.burger_constructor))
        assert driver.current_url == BASE + '/login', 'Регистрация нового пользователя'
        # Хоть убей не пойму, почему не переходит. Уже перепробовал все WebDriverWait, но думаю проблема не в нем

    def test_register_unvalid(self, driver):
        driver.get(REGISTER)
        driver.find_element(*L.register_name).send_keys('vlad')
        driver.find_element(*L.login_email).send_keys(str(randint(000000, 999999)) + '@.com')
        driver.find_element(*L.register_password).send_keys('123')
        driver.find_element(*L.register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.text_error_register))
        error_text = driver.find_element(*L.text_error_register).text
        assert error_text == 'Некорректный пароль', 'Некорректный пароль'

class TestLogIn:
    def test_login_from_main_page(self, driver):
        driver.get(BASE)
        driver.find_element(*L.login_button_in_main_page).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход по кнопке «Войти в аккаунт» на главной'

    def test_login_from_main_page_acc(self, driver):
        driver.get(BASE)
        driver.find_element(*L.acc_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку «Личный кабинет»'

    def test_login_from_register_page(self, driver):
        driver.get(REGISTER)
        driver.find_element(*L.button_login_in_register).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку в форме регистрации'

    def test_login_from_forgot_password(self, driver):
        driver.get(FORGOT_PASSWORD)
        driver.find_element(*L.button_login_in_register).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.login_button))
        driver.find_element(*L.login_email).send_keys(LOGIN)
        driver.find_element(*L.password).send_keys(PASSWORD)
        driver.find_element(*L.login_button).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        to_check = driver.find_element(*L.acc_button).text
        assert 'Личный Кабинет' == to_check, 'вход через кнопку в форме восстановления пароля'

class TestAcc:
    def test_acc_profile(self, valid_register):
        valid_register.find_element(*L.acc_button).click()
        WebDriverWait(valid_register, 3).until(EC.url_changes(ACCOUNT))
        assert valid_register.current_url == ACCOUNT_PROFILE, 'Переход в лк через клик кнопки «Личный кабинет»'

class TestMoveFromAcc:

    def test_move_by_constructor(self, valid_register):
        valid_register.find_element(*L.acc_button).click()
        valid_register.find_element(*L.burger_constructor).click()
        WebDriverWait(valid_register, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        constructor_h1 = valid_register.find_element(*L.constructor_h1_text).text
        assert constructor_h1 == 'Соберите бургер', 'Переход с лк в конструктор через кнопку "Конструктор"'

    def test_move_by_logo(self, valid_register):
        valid_register.find_element(*L.acc_button).click()
        valid_register.find_element(*L.logo_burger).click()
        WebDriverWait(valid_register, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        constructor_h1 = valid_register.find_element(*L.constructor_h1_text).text
        assert constructor_h1 == 'Соберите бургер', 'Переход с личного кабинета в конструктор через логотип сайта'

class TestLogoutFromAcc:
    def test_logout_from_acc(self, valid_register):
        valid_register.find_element(*L.acc_button).click()
        WebDriverWait(valid_register, 3).until(EC.url_changes(ACCOUNT))
        valid_register.find_element(*L.logout_button).click()
        WebDriverWait(valid_register, 3).until(EC.visibility_of_element_located(L.login_button))
        assert valid_register.current_url == LOGIN_PAGE, 'выход по кнопке «Выйти» в личном кабинете'

class TestConstructorBurger:
    def test_go_to_sauces_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        filter = driver.find_element(*L.sauces_filter).text
        assert filter == 'Соусы', 'Переход в раздел "Соусы"'
    def test_go_to_buns_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        driver.find_element(*L.buns_filter).click()
        filter = driver.find_element(*L.buns_filter).text
        assert filter == 'Булки', 'Переход в раздел "Булки"'
    def test_go_to_fillings_tab(self, driver):
        driver.find_element(*L.fillings_filter).click()
        filter = driver.find_element(*L.fillings_filter).text
        assert filter == 'Начинки', 'Переход в раздел "Начинки" '

