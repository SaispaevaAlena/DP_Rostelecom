import os
from dotenv import load_dotenv

# Подгружаем учетные записи из .env
load_dotenv()

# CONSTANTS CLASS
class RTC():  # RTC - RosTeleCom

    # Rostelecom products:
    URL_ELK_WEB = 'https://lk.rt.ru/'
    URL_ONLIME_WEB = 'https://my.rt.ru/'
    URL_START_WEB = 'https://start.rt.ru/'
    URL_SMARTHOME_WEB = 'https://lk.smarthome.rt.ru/'
    URL_KEY_WEB = 'https://key.rt.ru/'

    # joe doe - valid account:
    VALID_EMAIL = os.getenv('VALID_EMAIL')
    VALID_LOGIN = os.getenv('VALID_LOGIN')
    VALID_PASSWORD = os.getenv('VALID_PASSWORD')

    # some verified passws:
    VALID_PASSWORD_8 = "_=d;-A#b"  # 8 symbols
    VALID_PASSWORD_20 = "$b_.A|S!-=/-a+,A`S|?"  # 20 symbols

    # some unverified email, login and pass
    INVALID_EMAIL = 'joe.doee@1secmail.com'
    INVALID_LOGIN = 'rtkee_1680847166060'
    INVALID_PASSWORD = 'AscWdvEfb1!'

    # Cookies file name
    COOKIES_FILE = 'rtc_cookies.txt'

    # some inscriptions
    REGISTRATION_TEXT = "Регистрация"
    REGISTER_BUTTON_TEXT = "Зарегистрироваться"
    RECOVERY_INSCRIPTION_TEXT = "Восстановление пароля"
    RECOVERY_CAPTCHA_TEXT = "Символы"
    AUTH_BY_CODE_TEXT = "Авторизация по коду"
    AUTH_GET_CODE = "Получить код"
    AUTH_BY_PASS_TEXT = "Авторизация"
    ENTER_TEXT = "Войти"
    ERROR_NOTIFICATION_TEXT = "Неверный логин или пароль"
    PERSONAL_CABINET_TEXT = "Личный кабинет"