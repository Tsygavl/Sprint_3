from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_registration_success(self, driver):
        driver.find_element(*Locators.ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys('Влад')
        driver.find_element(*Locators.EMAIL).send_keys('tsygankovvlad@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('tsygankovvlad@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.ENT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_changes('https://stellarburgers.nomoreparties.site'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site' 'Успешная регистрация пользователя'

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*Locators.ACC_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('test@mail.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.ENT_BUTTON).click()
        driver.find_element(*Locators.INCORECT_PASSWORD_TEXT)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.INCORECT_PASSWORD_TEXT))
        reg_text = driver.find_element(*Locators.INCORECT_PASSWORD_TEXT).text
        assert reg_text == 'Некорректный пароль'