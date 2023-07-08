import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from url import URL

class TestLogoutFromAcc:
    def test_logout_from_acc(self, valid_sign_in):
        valid_sign_in.find_element(*L.acc_button).click()
        WebDriverWait(valid_sign_in, 3).until(EC.url_changes(URL.ACCOUNT))
        valid_sign_in.find_element(*L.logout_button).click()
        WebDriverWait(valid_sign_in, 3).until(EC.visibility_of_element_located(L.login_button))
        assert valid_sign_in.current_url == URL.LOGIN_PAGE, 'выход по кнопке «Выйти» в личном кабинете'