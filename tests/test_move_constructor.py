import pytest
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorBurger:
    def test_go_to_sauces_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.sauces))
        element_inside = WebDriverWait(driver,3).until(EC.visibility_of_element_located(L.sauces))
        text_element = element_inside.text
        assert text_element == 'Соусы', 'Переход в раздел "Соусы"'

    def test_go_to_buns_tab(self, driver):
        driver.find_element(*L.sauces_filter).click()
        driver.find_element(*L.buns_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.buns))
        element_inside = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.buns))
        text_element = element_inside.text
        assert text_element == 'Булки', 'Переход в раздел "Булки"'

    def test_go_to_fillings_tab(self, driver):
        driver.find_element(*L.fillings_filter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.fillings))
        element_inside = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(L.fillings))
        text_element = element_inside.text
        assert text_element == 'Начинки', 'Переход в раздел "Начинки"'
