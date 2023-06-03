from selenium.webdriver.common.by import By

class Locators:
    # Личный кабинет
    ACC_BUTTON = (By.XPATH, "//a[@href = '/account']")
    # Кнопка Зарегистрироваться
    REG_BUTTON = (By.XPATH, "//a[@href='/register']")
    # Кнопка Войти
    ENT_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    # Кнопка-огурец Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
    # Кнопка Восстановить
    RECOVER_BUTTON = (By.XPATH, '//button[contains(text(),"Восстановить")]')
    # Кнопка Сохранить
    SAVE_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')
    # Текст - "Некорректный пароль"
    INCORECT_PASSWORD_TEXT = (By.XPATH,'//p[@class="input__error text_type_main-default"]')
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]/parent::a")
    # логотип Stellar Burgers
    LOGO_BUTTON =  (By.XPATH, "//div[contains(@class, 'logo')]/a")
    # Кнопка Выход
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    # Секция Соусы
    SAUSE_SECTIONS = (By.XPATH, '//span[contains(text(),"Соусы")]')
    # Секция Булки
    BUNS_SECTIONS = (By.XPATH, '//span[contains(text(),"Булки")]')
    # Секция Начинки
    TOPPING_SECTIONS = (By.XPATH, '//span[contains(text(),"Начинки")]')
    # Заголовок Булки
    BUNS_HEADING = (By.XPATH, "//h2[contains(text(),'Булки')]")
    # Заголовок Соусы
    SAUSE_HEADING = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    # Заголовок Начинки
    TOPPING_HEADING = (By.XPATH, "//h2[contains(text(),'Начинки')]")
    # email
    EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    # password
    PASSWORD = (By.XPATH, "//label[contains(text(),'Пароль')]")
    # name
    NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    # Поле Восстановить пароль
    CODE_RECOVER = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    # Кнопка "Войти" в востановление пароля"
    BUTTON_COME_IN = (By.XPATH, "//a[@href='/login']")