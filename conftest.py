import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site'

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()

class VALID_ACC:
    email = "vlad_tsygankov_111@mail.ru"
    password = "123456"
