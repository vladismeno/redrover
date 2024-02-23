import math
# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']

# print(*my_list[2], sep=',')

# for i in my_list[2]:
#     print(i)


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100, 5.3]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

import numbers

#
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100, 5.3]

# res = sum([item for item in list_1 if isinstance(item, numbers.Number)])
# print(res)

# res = [item for item in list_1 if not isinstance(item, numbers.Number) and 'a' in item]
# print(res)
# print("Все строки, где есть буква 'a':", [x for x in list_1 if type(x) == str and 'a' in x])

#
# sum = 0
# for i in range(len(list_1)):
#     if type(list_1[i]) == int:
#         sum += list_1[i]
# print(sum)
#
# def sum_list(my_list):
#     sum = 0
#     for value in my_list:
#         if isinstance(value, numbers.Number):
#             sum += value
#
#     return sum
#
#
# def find_a(my_list, char):
#     for item in my_list:
#         if isinstance(item, numbers.Number):
#             continue
#         if char in item:
#             print(item)
#
#
# res_sum = sum_list(list_1)
# print(f'Сумма чисел: {res_sum}')
# print(f'Поиск символов \'a\':')
# find_a(list_1, 'a')


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

# list = ['cat', 'dog', 'horse', 'cow']
# print(type(list))
# print(type(tuple(list)))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family1 = input("Введите через запятую всех членов семьи1: ")
# family2 = input("Введите через запятую всех членов семьи2: ")
# list1 = family1.split(',')
# list2 = family2.split(',')
# len1 = len(list1)
# len2 = len(list2)
# if len1 > len2:
#     print(family1)
# elif len2 > len1:
#     print(family2)
# else:
#     print("Equal")


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# dict = {
#     'title': 'The best film',
#     'director': 'Vlad',
#     'year': 1987,
#     'budget': 20000,
#     'main_actor': 'Uksus',
#     'slogan': 'Hello world!',
# }
#
# print(dict.keys())
#
# print(dict.values())

# for k in dict:
#     print(f'key: {k}')
#
# for k in dict:
#     print(f'value: {dict[k]}')
#
# for k in dict:
#     print(f'{k}={dict[k]}')

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# list1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(list(set(list1)))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {1, 2, 3}
set2 = {1, 2, 4}
# print(set1.intersection(set2))
# print(set1.issubset(set2)) # входит ли set1 в set2
# print(set1.issuperset(set2)) # входит ли set2 в set1

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# print(set1.intersection(set2))
print(set1.difference(set2).union(set2.difference(set1)))


# set1 = {'a', 1, 'c'}
# set2 = {'a', 1, 'c'}
#
# len1 = len(set1)
# len2 = len(set2)
# if len1 > len2 and len(set2.intersection(set1)) == len2:
#     print(f'set1:{set1} содержит set2: {set2}')
# elif len2 > len1 and len(set1.intersection(set2)) == len1:
#     print(f'set2:{set2} содержит set1: {set1}')
# elif len1 == len2 and len(set1.intersection(set2)) == len1:
#     print(f'set1:{set1} = set2: {set2}')
# else:
#     print('set1 не является подмножеством set2 и наоборот')