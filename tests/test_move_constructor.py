import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorBurger:
    def test_go_to_sauces_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.sauces))
        filter = driver.find_element(*L.sauces).text
        assert filter == 'Соусы', 'Переход в раздел "Соусы"'

    def test_go_to_buns_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        driver.find_element(*L.buns_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.buns))
        filter = driver.find_element(*L.buns).text
        assert filter == 'Булки', 'Переход в раздел "Булки"'

    def test_go_to_fillings_tab(self, driver):
        driver.find_element(*L.fillings_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.fillings))
        filter = driver.find_element(*L.fillings).text
        assert filter == 'Начинки', 'Переход в раздел "Начинки"'
