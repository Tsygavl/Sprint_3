from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import VALID_ACC as VA


def test_constructor_button_tap(self, driver):
    driver.get('https://stellarburgers.nomoreparties.site/account/profile')
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Проверка перехода страницы по кнопку "Конструктор"'

def test_change_section_sause(self, driver):
    driver.find_element(*Locators.SAUSE_SECTIONS).click
    section_name = driver.find_element(*Locators.SAUSE_HEADING).text()
    assert section_name == 'Соусы' 'Переход к разделу "Соусы"'

def test_change_section_buns(self, driver):
    driver.find_element(*Locators.BUNS_SECTIONS).click()
    section_name = driver.find_element(*Locators.BUNS_HEADING).text()
    assert section_name == 'Булки' 'Переход к разделу "Булки"'

def test_change_section_topping(self, driver):
    driver.find_element(*Locators.TOPPING_SECTIONS).click
    section_name = driver.find_element(*Locators.TOPPING_HEADING).text()
    assert section_name == 'Начинки' 'Переход к разделу "Начинки"'