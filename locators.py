from selenium.webdriver.common.by import By

class Locators:
    login_email = By.XPATH, "//label[text() = 'Email']/parent::div/input"  #Ввод имейл для входа и регистрации
    password = By.XPATH, ".//input[@type=\'password\' and @name=\'Пароль\']"  # Ввод пароля для входа
    login_button = By.XPATH, ".//button[text()=\'Войти\']"  # Кнопка "Войти" авторизации
    register_name = By.XPATH, "//label[text() = 'Имя']/parent::div/input"  # Ввод имени при регистрации
    register_button = By.XPATH, "//button[text()='Зарегистрироваться']"  # кнопка регистрации
    register_password = By.NAME, "Пароль"  #Ввод пароля при регистрации
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
    sauces = By.XPATH, "//h2[contains(text(),'Соусы')]" # h2 Соусы
    buns = By.XPATH, "//h2[contains(text(),'Булки')]" # h2 Булки
    fillings = By.XPATH, "//h2[contains(text(),'Начинки')]" # h2 Начинки
    login_title = (By.XPATH, "//h2[text()='Вход']")
