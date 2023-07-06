from selenium.webdriver.common.by import By

class Locators:
    login_email = By.XPATH, "//label[text() = 'Email']/parent::div/input"  #Ввод имейл для входа и регистрации
    password = By.XPATH, ".//input[@type=\'password\' and @name=\'Пароль\']"  # Ввод пароля для входа
    login_button = By.XPATH, ".//button[text()=\'Войти\']" # Кнопка "Войти" авторизации
    register_name = By.XPATH, "//label[text() = 'Имя']/parent::div/input"  # Ввод имени при регистрации
    register_button = By.XPATH, "//button[text()='Зарегистрироваться']"  # кнопка регистрации
    register_password = By.NAME, "Пароль" #Ввод пароля при регистрации
    text_error_register = By.XPATH, "//p[text()='Некорректный пароль']"  # Ошибка "Некорректный пароль" при регистрации
    login_button_in_main_page = By.XPATH, "// button[text() = 'Войти в аккаунт']"  # Кнопка "Войти в Аккаунт" на главной странице
    burger_constructor = By.XPATH, "//p[contains(text(),'Конструктор')]/parent::a"  # Кнопа "Конструктор"
    constructor_h1_text = By.XPATH, "// h1[text()='Соберите бургер']"
    acc_button = By.XPATH, "//a[@href = '/account']"  # Кнопка "Личный кабинет"
    button_login_in_register = By.XPATH, "//a[@href = '/login']"  # Кнопка "Войти" на странице регистрации
    button_forgot_password = By.XPATH, "//a[@href = '/forgot-password']"  # Кнопка "Восстановить пароль"
    logo_burger = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"  # логотип
    logout_button = By.XPATH, ".//button[text() = 'Выход']" # кнопка выйти
    sauces_filter = By.XPATH, '//span[contains(text(),"Соусы")]'  # Фильтр Соусы
    buns_filter = By.XPATH, '//span[contains(text(),"Булки")]'  # Фильтр Булки
    fillings_filter = By.XPATH, '//span[contains(text(),"Начинки")]'  # Фильтр Начинки

    # Личный кабинет
    ACC_BUTTON = (By.XPATH, "//a[@href = '/account']")
    # Кнопка Зарегистрироваться
    REG_BUTTON = (By.XPATH, "//a[@href='/register']")
    # Кнопка Войти
    ENT_BUTTON = ()
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
    # name
    NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    # Поле Восстановить пароль
    CODE_RECOVER = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    # Кнопка "Войти" в востановление пароля"
    BUTTON_COME_IN = (By.XPATH, "//a[@href='/login']")