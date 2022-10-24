"""Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

# import random
#
# def sum_of_odd_numbers(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#
#     return sum
#
# def create_random_list(size):
#     list = []
#     for i in range(size):
#         list.append(random.randint(1, 100))
#
#     return list
#
# try:
#     size_list = int(input('Введите размер списка: '))
#     list = create_random_list(size_list)
#     print(f'Исходный список: {list}')
#     print(f'Сумма элементов на нечетных позициях равна {sum_of_odd_numbers(list)}')
#
# except:
#     print('Введите целое число.')


"""Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

# import random
#
# def create_random_list(size):
#     list = []
#     for i in range(size):
#         list.append(random.randint(1, 10))
#
#     return list
#
# def multi_pair_values(list):
#     multi_list = []
#     for i in range(len(list) // 2 + len(list) % 2):
#         multi_list.append(list[i] * list[(-i) - 1])
#
#     return multi_list
#
# try:
#     size_list = int(input('Введите размер списка: '))
#     list = create_random_list(size_list)
#     print(f'Исходный список: {list}')
#     new_list = multi_pair_values(list)
#     print(f'Список из произведений пар чисел исходного списка: {new_list}')
#
# except:
#     print('Введите целое число.')


"""Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

# import random
#
# def create_random_float_list(size):
#     list = []
#     for i in range(size):
#         integer_value = random.randint(1, 10)
#         fraction_value = float(random.randint(1, 100))
#         while fraction_value > 1:
#             fraction_value /= 10
#         list.append(integer_value + fraction_value)
#
#     return list
#
# def difference_max_fraction_and_min_fraction(list):
#     new_list = []
#     for i in range(len(list)):
#         new_list.append(list[i] % 1)
#
#     max = new_list[0]
#     min = new_list[-1]
#     for i in new_list:
#         if i > max:
#             max = i
#         elif i < min:
#             min = i
#
#     return max - min
#
# try:
#     size_list = int(input('Введите размер списка: '))
#     list = create_random_float_list(size_list)
#     print(f'Исходный список: {list}')
#     print(f'Разница между максимальным и минимальным значением дробной части элементов равна '
#           f'{round(difference_max_fraction_and_min_fraction(list), 3)}')
#
# except:
#     print('Введите целое число.')


"""Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать 
готовые функции.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10"""

# def convert_to_binary_number(num):
#     binary = ''
#     while num != 0:
#         binary += str(num % 2)
#         num //= 2
#
#     return binary[::-1]
#
# try:
#     number = int(input('Введите целое число: '))
#     print(f'{number} в двоичной системе будет равно {convert_to_binary_number(number)}')
#
# except:
#     print('Введите целое число!')

"""задача5 HARD необязательная.
Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб количество 
элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем 
чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три 
на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу."""

# import random
#
# def create_random_array(rows, columns):
#     if (rows * columns) % 2 == 0:
#         array = [[random.randint(10, 99) for i in range(columns)] for j in range(rows)]
#         return array
#     else:
#         print('Количество элементов нечетное.')
#         return exit()
#
# def show_2d_array(array):
#     string = ''
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             string += str(array[i][j]) + ' '
#         print(string)
#         string = ''
#
# def unsort_array(array):
#     list = []
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             temp = array[i][j]
#             list.append(temp)
#
#     index = []
#     for n in range(len(list)):
#         index.append(n)
#
#     size = index[-1]
#     for k in range(int((len(list) / 2))):
#         if k in index:
#             index.remove(k)
#             while True:
#                 l = random.randint((size + 1) / 2, size)
#                 if l in index:
#                     index.remove(l)
#                     temp = list[k]
#                     list[k] = list[l]
#                     list[l] = temp
#                     break
#     n = 0
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             array[i][j] = list[n]
#             n += 1
#
#     return array
#
#
# row = int(input('Введите количество строк: '))
# column = int(input('Введите количество столбцов: '))
# array = create_random_array(row, column)
# print()
# print(f'Исходный массив:')
# show_2d_array(array)
# print()
# new_array = unsort_array(array)
# print(f'Перемешаный:')
# show_2d_array(new_array)