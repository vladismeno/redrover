# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую
# 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
import time

# set = {1,2,3} #множество можно менять
# list = [1,2,3] #список можно менять
# tuple = (1,2,3) #кортеж, нельзя менять
# dict = {'test': (1,2,3)} #словарь
# dict = {'test': [1,2,3]} #словарь
# dict = {'test': {1,2,3}} #словарь

# side = float(input("Введите сторону квадрата: "))
# pr = side * 4
# pl = side ** 2
# d = side * 2 ** 0.5
# my_tuple = (pr, pl, d)
# print(my_tuple)


# 4.2. Напишите функцию, которая принимает произвольное количество именованных аргументов и выводит
# их построчно в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def my_print(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
#
# my_print(name='John', last_name='Smith', age=35, position='web developer')


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа

# list_before = [20, -3, 15, 2, -1, -21]
#
# positive_numbers = lambda my_list: [i for i in my_list if i > 0]
# print(positive_numbers(list_before))
#
# print(list(filter(lambda v: v > 0, list_before)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
# from functools import reduce
#
# list_before = [20, -3, 15, 2, -1, -21]
# print(reduce(lambda a, b: a * b, list_before))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

# import time
#
#
# def count_execution_time(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         func(*args)
#         end = time.perf_counter()
#         result = end - start
#         print(f'Время выполнения функции: {result} секунд')
#     return wrapper
#
#
# @count_execution_time
# def my_func(name, surname):
#     print(f'Hello world, my name is {name} {surname}!')
#     time.sleep(1)
#
# my_func('Vladislav', 'Semenov')

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

from my_calc import *

a = float(input('Введите a: '))
b = float(input('Введите b: '))

print(func_sum(a, b))
print(func_difference(a, b))
print(func_divide(a, b))
print(func_multiply(a, b))
