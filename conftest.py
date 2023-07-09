import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import LOGIN, PASSWORD
from url import URL
from locators import Locators as L


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL.BASE)
    yield driver
    driver.quit()


@pytest.fixture()
def valid_sign_in(driver):
    driver.get(URL.LOGIN_PAGE)
    driver.find_element(*L.login_email).send_keys(LOGIN)
    driver.find_element(*L.password).send_keys(PASSWORD)
    driver.find_element(*L.login_button).click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
    return driver
