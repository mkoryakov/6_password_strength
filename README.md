# 6_password_strength
Скрипт вычисляет сложность пароля, поданного на вход. Результат выводится в диапазоне [1, 10], где 1 - очень слабый пароль, 10 - очень сильный.
Также на вход скрипту необходимо подать файл, содержащий список наиболее часто используемых паролей. blacklist с паролями можно найти по адресу https://github.com/danielmiessler/SecLists/tree/master/Passwords.

Пример запуска скрипта:
python password_strength.py --password your_password --blacklist path_to_password_blacklist
