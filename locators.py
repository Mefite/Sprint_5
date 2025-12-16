from selenium.webdriver.common.by import By

class Locators:
     # Кнопка "Вход и регистрация" на главной странице
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Вход и регистрация']"
     # Кнопка "Нет аккаунта" на форме входа 
    NO_ACC_BUTTON = By.XPATH, "//button[text() = 'Нет аккаунта']"
     # Поле ввода email на форме регистрации
    INPUT_EMAIL = By.XPATH, "//input[@name='email']"
     # Поле ввода пароля на форме регистрации
    INPUT_PASSWORD = By.XPATH, "//input[@name = 'password']"
     # Кнопка "Войти" на странице входа
    FORM_LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"
     # Поле подтверждения пароля на форме входа и регистрации
    INPUT_REPEAT_PASSWORD = By.XPATH, "//input[@name = 'submitPassword']"
     # Кнопка "Создать аккаунт" в форме регистрации
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//button[text() = 'Создать аккаунт']"
     # Аватар пользователя 
    USER_AVATAR = By.XPATH, "//button[@class='circleSmall']"
     # Имя пользователя 
    USER_NAME = By.XPATH, "//h3[@class = 'profileText name']"
     # Сообщение об ошибке под полем ввода почты
    ERROR_EMAIL = By.XPATH, "//span[text() = 'Ошибка']"
     #  Кнопка "Выйти" на главной странице
    LOGOUT_BUTTON = By.XPATH, "//button[text() = 'Выйти']"
     # Кнопка "Разместить объявление"
    ADS_BUTTON = By.XPATH, "//button[text() = 'Разместить объявление']"
     # Поле "Название" объявления
    INPUT_ADS_TITLE = By.XPATH, "//input[@placeholder = 'Название']"
     # Кнопка выпадающего списка категории
    CATEGORY_BUTTON = By.XPATH, "//input[@name='category']/../button"
     # Категория "Авто" выпадающего списка
    CHOICE_CATEGORY = By.XPATH, "//span[text()= 'Авто']"
     # кнопка "Б/У" 
    CONDITION_BUTTON_OLD = By.XPATH, "//input[@value='Б/У']/.."
     # Кнопка выпадающего списка город
    CITY_BUTTON = By.XPATH, "//input[@name = 'city']/../button"
     # Город Казань в выпадающем списке
    CHOICE_CITY = By.XPATH, "//span[text()= 'Казань']"
     # Поле "Описание товара" объявления 
    INPUT_ADS_DESCRIPTION = By.XPATH, "//textarea[@name='description']"
     # Поле "Стоимость" объявления
    INPUT_ADS_PRICE = By.XPATH, "//input[@name = 'price']"
     # Кнопка "Опубликовать" объявление
    PUBLISH_BUTTON = By.XPATH, "//button[text() = 'Опубликовать']"
     # Раздел "Мои объявления" в профиле
    MY_ADS = By.XPATH, "//div[@class='card']//h2[text()= 'DeLorean']"
     # Заголовок окна авторизации для размещения объявления
    AUTH_ADS = By.XPATH, "//h1[text()= 'Чтобы разместить объявление, авторизуйтесь']"






    


