# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
# для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

my_list = [1, 1.1, 'Привет', True, False]
print(f'Наш список: {my_list}\n')
for i in my_list:
    print(f'Число {i}  тип {type(i)}')

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_count = int(input("\nВведите количество элементов списка "))
my_list = []
i = 0

while i < list_count:
    my_list.append(input("Введите значение списка "))
    i += 1
print(f'Ваш список: {my_list}\n')
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        element = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = element
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        element = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = element
        i += 2
print(f'Ваш список при обмене значений соседних элементов: {my_list}\n')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = int(input("Введите месяц, используя число: "))

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень '}

if month == 12 or month == 1 or month == 2:
    print(f'Это время года по методу dict: {seasons_dict.get(1)}')
    print(f'Это время года по методу list: {seasons_list[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Это время года по методу dict: {seasons_dict.get(2)}')
    print(f'Это время года по методу list: {seasons_list[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Это время года по методу dict: {seasons_dict.get(3)}')
    print(f'Это время года по методу list: {seasons_list[2]}')

elif month == 9 or month == 10 or month == 11:
    print(f'Это время года по методу dict: {seasons_dict.get(4)}')
    print(f'Это время года по методу list: {seasons_list[3]}')
else:
    print("Такого месяца не существует, нужно вводить числа от 1 до 12")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
print('\n')
my_str = input('Введите предложение: ')
a = my_str.split(' ')
for i, elment in enumerate(a, 1):
    if len(elment) > 10:
        el = elment[0:10]
    print(f'{i}. - {elment}')

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
print('\n')
number = int(input("Веведите номер: "))
my_list = [7, 5, 3, 3, 2]
count_list = my_list.count(number)
for element in my_list:
    if count_list > 0:
        i = my_list.index(number)
        my_list.insert(i + count_list, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
