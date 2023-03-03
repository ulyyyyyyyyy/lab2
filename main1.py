'''При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности,
 поскольку такой подход уменьшает возможность неверного ввода пароля.
 Напишите программу, которая сравнивает пароль и его подтверждение.
 Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».'''
password = input("Введите пароль")

is_numeric = False
is_upper = False
is_lower = False
is_spec = False

for char in password:
    if char.isnumeric():
        is_numeric = True
    elif char.islower():
        is_lower = True
    elif char.isupper():
        is_upper = True
    elif char in "@#$%^&*!":
        is_spec = True


if len(password) > 5 and is_numeric and is_upper and is_lower and is_spec:
    print("Пароль: ОК")
else:
    print("Пароль ненадежный")
    password = input("введите пароль")

password2 = input("Повторите пароль")

if password == password2:
    print("Пароли совпадают")
else:
    print("Пароли не совпадают")
    password2 = input("Повторите пароль")

if password == password2:
    print("Пароли совпадают")