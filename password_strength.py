import argparse
import re


def is_password_include_words_form_blacklist(password):
    blacklist = ['password', 'user', 'asdf', 'qwerty', 'wasd', 'jkl;', 'zxcvb']
    password_in_lower_chars = password.lower()
    for word in blacklist:
        if word in password_in_lower_chars:
            return True
    return False


def is_password_include_date(password):
    years = range(1900, 2016)
    for year in years:
        if str(year) in password:
            return True
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun;', 'jul', 'aug',
              'sep', 'oct', 'nov', 'dec']
    password_in_lower_chars = password.lower()
    for month in months:
        if month in password_in_lower_chars:
            return True
    return False


def is_password_include_name(password):
    names = ['masha', 'sasha', 'pasha', 'dasha', 'vanya', 'katya;',
             'zhenya', 'lena', 'petya', 'anna', 'dima', 'vika']
    password_in_lower_chars = password.lower()
    for name in names:
        if name in password_in_lower_chars:
            return True
    return False


def get_password_strength(password):
    # шаблон для проверки на вхождение в пароль номеров
    # телефона, лицензий и т.д.
    re_pattern = re.compile('\d{5,}')
    if len(password) < 5:
        if password.isdigit():
            return 1
        else:
            return 2
    elif 5 <= len(password) < 8 and (is_password_include_name(password) or
                                     is_password_include_date(password) or
                                     is_password_include_words_form_blacklist(password) or
                                     re_pattern.search(password)):
        return 3
    elif (is_password_include_name(password) or
          is_password_include_date(password) or
          is_password_include_words_form_blacklist(password) or
          re_pattern.search(password)):
        password_strength = 4
    else:
        password_strength = 6

    for char in password:
        if char.isdigit():
            password_strength += 1
            break
    for char in password:
        if char.isalpha() and char.islower():
            password_strength += 1
            break
    for char in password:
        if char.isalpha() and char.isupper():
            password_strength += 1
            break
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                     '+', '-', '/', ':', ';', '=']
    for char in special_chars:
        if char in password:
            password_strength += 1
            break
    return password_strength


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Вычисление сложности
    пароля. Сложность оценивается по шкале от 1 до 10.''')
    parser.add_argument('--password', '-pass', default='Asd1r$._8765',
                        help='пароль для проверки сложности')
    args = parser.parse_args()
    password_strength = get_password_strength(args.password)
    print('Сложность пароля: %d' % password_strength)
