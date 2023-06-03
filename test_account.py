from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import VALID_ACC as VA

def test_account_tap(self, driver):
    driver.find_element(*Locators.ACC_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' 'Проверка перехода по клику "Личный кабинет"'

def test_logo_tap(self, driver):
    driver.get('https://stellarburgers.nomoreparties.site/account/profile')
    driver.find_element(*Locators.LOGO_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Проверка перехода страницы по логотипу'

def test_exit_button_tap(self, driver):
    driver.get('https://stellarburgers.nomoreparties.site/account/profile')
    driver.find_element(*Locators.EXIT_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' 'Проверка кнопки "Выйти" в личном кабинете'