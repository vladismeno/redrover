# 1.1
#     1) Установите Python и PyCharm
#     2) Напишите и запустите программу, которая выводит строку "Hello world!"
#     3) Напишите программу, которая на входе получает имя пользователя,
#     сохраняет его в переменную user_name и выводит строку "Hello {user_name}!"
#     4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую
#     операцию(на ваше усмотрение), и выводит “Результат = {результат}”.

# print("Hello world!")

# user_name = input("Введите имя пользователя: ")
# print(f"Hello {user_name}!")


# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# c = a + b
# print(f"Результат a + b = {c}")


# 1.2
# 1) Напишите
# программу, чтобы вывести:
#
# *********
# *       *
# *       *
# *********


# print("*********")
# print("*       *")
# print("*       *")
# print("*********")

# 1.3. Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# Пример:
#
# Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8

# number = int(input("Введите четырехзначное число: "))
# if number < 1000 or number > 9999:
#     print("Введено неправильное число!")
# else:
#     thousands = number // 1000
#     hundreds = number % 1000 // 100
#     decimals = number % 1000 % 100 // 10
#     numbers = number % 1000 % 100 % 10
#     print(f'Тысячи: {thousands}')
#     print(f'Сотни: {hundreds}')
#     print(f'Десятки: {decimals}')
#     print(f'Единицы: {numbers}')


# 1.4. Напишите программу, которая считывает два целых числа a и b
# и выводит на экран квадрат суммы (a+b)2 и сумму квадратов a2+b2 этих чисел.

# Пример:
#
# Input:
# 3
# 2
#
# Output:
# Квадрат суммы 3 и 2 равен 25
# Сумма квадратов 3 и 2 равна 13

# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# res1 = (a + b) ** 2
# res2 = a ** 2 + b ** 2
# print(f'Квадрат суммы {a} и {b} равен {res1}')
# print(f'Сумма квадратов {a} и {b} равна {res2}')

