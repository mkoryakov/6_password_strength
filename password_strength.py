import argparse
import os.path
import re


def get_passwords_from_blacklist(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as file_handler:
        return file_handler.readlines()


def is_password_in_blacklist(password, blacklist_handler):
    password_in_lower_chars = password.lower()
    for word in blacklist_handler:
        if word.rstrip() == password_in_lower_chars:
            return True
    return False


def is_password_include_word_from_blacklist(password, blacklist_handler):
    password_in_lower_chars = password.lower()
    for word in blacklist_handler:
        if word.rstrip() in password_in_lower_chars:
            return True
    return False


def get_password_strength(password, passwords_from_blacklist):
    length_weak_password = 5
    length_middle_password = 8
    length_strong_password = 12
    phone_pattern = re.compile('\d{5,}')
    is_phone_in_password = phone_pattern.search(password)
    is_bad_password = is_password_include_word_from_blacklist(password,
                                                              passwords_from_blacklist)
    password_length = len(password)
    if is_password_in_blacklist(password, passwords_from_blacklist):
        return 1
    if password_length < length_weak_password:
        if password.isdigit():
            return 1
        else:
            return 2
    elif password_length < length_middle_password:
        if is_phone_in_password or is_bad_password:
            return 3
        else:
            password_strength = 3
    elif password_length < length_strong_password:
        if is_phone_in_password or is_bad_password:
            return 4
        else:
            password_strength = 4
    else:
        if is_phone_in_password or is_bad_password:
            return 5
        else:
            password_strength = 5

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
    latin_pattern = re.compile('[a-zA-Z]')
    cyrillic_pattern = re.compile('[а-яА-Я]')
    if latin_pattern.search(password) and cyrillic_pattern.search(password):
        password_strength += 1
    return password_strength


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Вычисление сложности
    пароля. Сложность оценивается по шкале от 1 до 10.''')
    parser.add_argument('--password', '-pass', default='Qdf1iЯwd$._87',
                        help='пароль для проверки сложности')
    parser.add_argument('--blacklist', '-bl',
                        default='10_million_password_list_top_1000.txt',
                        help='файл, содержащий пароли из черного списка')
    args = parser.parse_args()
    passwords_from_blacklist = get_passwords_from_blacklist(args.blacklist)
    password_strength = get_password_strength(args.password,
                                              passwords_from_blacklist)
    print('Сложность пароля: %d' % password_strength)
