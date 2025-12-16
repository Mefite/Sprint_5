import random
import string

def generate_email(domain="yandex.ru", username_length=8):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    email = f"{username}@{domain}"
    return email

class PersonalData():
    user_password = "password5"
    user_email = "mailsprint5@mail.ru"

class URL():
    test_url = 'https://qa-desk.stand.praktikum-services.ru'
    
