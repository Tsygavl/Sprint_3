import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE, LOGIN_PAGE, LOGIN, PASSWORD
from locators import Locators as L


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE)
    yield driver
    driver.quit()


@pytest.fixture()
def valid_register(driver):
    driver.get(LOGIN_PAGE)
    driver.find_element(*L.login_email).send_keys(LOGIN)
    driver.find_element(*L.password).send_keys(PASSWORD)
    driver.find_element(*L.login_button).click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.burger_constructor))
    return driver
