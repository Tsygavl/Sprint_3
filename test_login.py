from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import VALID_ACC as VA
from selenium.webdriver.support.wait import WebDriverWait

from conftest import VALID_ACC as VA
from locators import Locators


def test_login_with_account_button(self, driver):
    driver.find_element(*Locators.ACC_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(VA.email)
    driver.find_element(*Locators.PASSWORD).send_keys(VA.password)
    driver.find_element(*Locators.ENT_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Вход в аккаунт с главной страницы'


def test_login_with_registration_button(self, driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*Locators.NAME).send_keys('Влад')
    driver.find_element(*Locators.EMAIL).send_keys('tsyfake@mail.ru')
    driver.find_element(*Locators.PASSWORD).send_keys('123456')
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(VA.email)
    driver.find_element(*Locators.PASSWORD).send_keys(VA.password)
    driver.find_element(*Locators.ENT_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Вход в аккаунт с страницы регистрации'


def test_login_with_forgot_password_button(self, driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(*Locators.NAME).send_keys(VA.email)
    driver.find_element(*Locators.RECOVER_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'
    driver.find_element(*Locators.PASSWORD).send_keys('123456789')
    driver.find_element(*Locators.CODE_RECOVER).send_keys('12345test')
    driver.find_element(*Locators.BUTTON_COME_IN).click()
    WebDriverWait(driver, 3)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Вход через кнопку "Войти" в востановления пароля'