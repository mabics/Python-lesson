# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
print('Задание 1')
def dev_print(a, b):
    if b != 0:
        dev = a / b
        return dev

    else:
        print('На ноль делить нельзя!')


a = int(input('a='))
b = int(input('b='))
dev = dev_print(a, b)
if b != 0:
    print(dev)

print('\nЗадание 2')
# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def data_users(name, lastname, year_of_birth, city, email, phone):
    return print(f'{name} {lastname}, {year_of_birth} г.р., г. {city}, {email}, с.т. {phone}')


data_users(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

print('\nЗадание 3')
def my_func(a, b, c):
    print(f'Сумма двух наибольших аргументов равна: {a + b + c - min([a, b, c])}')


my_func(
    int(input('a:')),
    int(input('b:')),
    int(input('c:')),
)

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

print('\nЗадание 4')

