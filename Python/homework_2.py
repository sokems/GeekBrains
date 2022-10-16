"""Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
Через строку нельзя решать."""

def sum_values(num):
    sum = 0
    current = 1
    check = 1
    if num % 10 != 0:
        while check != 0:
            check = (num % 10 ** current) // 10 ** (current - 1)
            sum += check
            current += 1
    else:
        current = 2
        while check != 0:
            check = (num % 10 ** current) // 10 ** (current - 1)
            sum += check
            current += 1
    return sum

try:
    num = str(float(input('Введите число: ')))
    new_num = int(num.replace('.',''))
    print(f'Сумма цифр равна {sum_values(new_num)}')

except:
    print('Введите число!')

"""Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

# def array_multi(num):
#     arr = [1] * num
#     for i in range(1, num + 1):
#         for j in range(1, i + 1):
#             arr[i - 1] *= j
#     return arr
# try:
#     num = int(input("Введите число: "))
#     print(array_multi(num))
#
# except:
#     print('Введите целое число!')

"""Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять 
количество вхождений одной строки в другой."""

# def count_find_str(str1, str2):
#     count = 0
#     if str2 in str1:
#         for i in range(len(str1)):
#             if str1[i] == str2[0]:
#                 if str1[i:i + len(str2)] == str2:
#                     count += 1
#     print(f'Строка "{str2}" встречается в строке "{str1}" {count} раз(-а).')
#
# try:
#     string1 = input('Введите 1 строку: ')
#     string2 = input('Введите 2 строку: ')
#
#     if len(string1) > len(string2):
#         count_find_str(string1, string2)
#     else:
#         count_find_str(string2, string1)
#
# except:
#     print('Строки нельзя оставлять пустыми!')

"""Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит
расстояние между ними в N-мерном пространстве."""

# def distance_between_points(point1, point2, size):
#     sum = 0
#     for i in range(size):
#         sum += (point1[i] - point2[i]) ** 2
#     return sum ** 0.5
#
# try:
#     size = int(input('Введите размерность: '))
#     point_first = []
#     point_second = []
#
#     for a in range(size):
#         point_first.append(int(input(f'Введите {a + 1} координату: ')))
#     for b in range(size):
#         point_second.append(int(input(f'Введите {b + 1} координату: ')))
#
#     print(f'Расстояние между точками {point_first} и {point_second} равно {distance_between_points(point_first, point_second, size)}.')
#
# except:
#     print('Некорректный ввод!')

"""Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов не три, а генерируется случайным образом 
от 5 до 25, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала 
программа."""

# import random, time
# def convert_value_to_bool(num):
#     if num == 1:
#         return True
#     elif num == 0:
#         return False
#
# time_start = time.process_time()
# number = random.randint(5, 25)
# preds = []
# check = 0
#
# for n in range(100):
#     preds.append(convert_value_to_bool(random.randint(0, 1)))
#     begin_left = preds[0]
#     right = not preds[0]
#
#     for i in range(1, number):
#         preds.append(convert_value_to_bool(random.randint(0, 1)))
#
#         begin_left = begin_left or preds[i]
#         left = not begin_left
#         right = right and not preds[i]
#
#     print(preds)
#
#     if (left != right):
#         check = 1
#         break
#
#     preds.clear()
#
# if check == 0:
#     print('Удтверждение истинно.')
# else:
#     print('Удтверждение ложно.')
#
# time_end = time.process_time()
# time = time_end - time_start
# print(time)