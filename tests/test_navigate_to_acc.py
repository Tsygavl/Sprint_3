import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from url import URL

class TestAcc:
    def test_acc_profile(self, valid_sign_in):
        valid_sign_in.find_element(*L.acc_button).click()
        WebDriverWait(valid_sign_in, 3).until(EC.url_changes(URL.ACCOUNT))
        assert valid_sign_in.current_url == URL.ACCOUNT_PROFILE, 'Переход в лк через клик кнопки «Личный кабинет»'

class TestMoveFromAcc:

    def test_move_by_constructor(self, valid_sign_in):
        valid_sign_in.find_element(*L.acc_button).click()
        valid_sign_in.find_element(*L.burger_constructor).click()
        WebDriverWait(valid_sign_in, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        constructor_h1 = valid_sign_in.find_element(*L.constructor_h1_text).text
        assert constructor_h1 == 'Соберите бургер', 'Переход с лк в конструктор через кнопку "Конструктор"'

    def test_move_by_logo(self, valid_sign_in):
        valid_sign_in.find_element(*L.acc_button).click()
        valid_sign_in.find_element(*L.logo_burger).click()
        WebDriverWait(valid_sign_in, 2).until(EC.visibility_of_element_located(L.burger_constructor))
        constructor_h1 = valid_sign_in.find_element(*L.constructor_h1_text).text
        assert constructor_h1 == 'Соберите бургер', 'Переход с лк в конструктор через логотип сайта'