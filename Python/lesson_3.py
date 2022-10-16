"""3. Задайте список из n чисел последовательности(1 + 1 / N) ** N и выведите на экран их сумму.

*Пример: *

- Для
n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}"""

# def list_posl(number):
#     list = []
#     for i in range(1, number + 1):
#         list.append(round((1 + 1 / i) ** i, 3))
#     return list
#
# def sum_values_list(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
#
# try:
#     num = int(input('Введите целое число: '))
#
#     print(f'Последовательность равна: {list_posl(num)}')
#     print(f'Сумма элементов равна {sum_values_list(list_posl(num))}')
#
#
# except:
#     print('Введите целое число.')

"""4. Задайте список из N элементов, заполненных числами из промежутка[-N, N].Найдите произведение элементов
на указанных позициях.Позиции хранятся в файле file.txt в одной строке одно число."""

import random

def create_list_random(number):
    list = []
    for i in range(number):
        list.append(random.randint(-number, number))
    return list

list = []
path = 'file.txt'
data = open(path, 'r')
for line in data:
    list.append(int(line))
data.close()

try:
    size = int(input('Введите число N: '))
    arr = create_list_random(size)
    print(arr)
    print(list)

except:
    print('Введите целое число!')

try:
    multi = 1
    for i in list:
        multi *= arr[i]
    print(f'Произведение равно {multi}')

except:
    print('Вы вышли за пределы списка.')

"""20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число."""

# def create_string_list(number):
#     list = []
#     for i in range(number):
#         list.append(input('Введите что-нибудь: '))
#     return list
#
# def check_value_in_list(list, number):
#     for i in list:
#         if i == number:
#             print('В списке присутствует ваше число!')
#
# try:
#     num = input('Введите искомое число: ')
#     size = int(input('Введите размер списка: '))
#     list = create_string_list(size)
#     check_value_in_list(list, num)
#
# except:
#     print('Некорректный ввод!')

"""21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
"""

# def create_string_list(number):
#     list = []
#     for i in range(number):
#         list.append(input('Введите что-нибудь: '))
#     return list
#
# def check_double_first_value(list, find):
#     check = 0
#     find_index = -1
#     for i in range(len(list)):
#         if list[i] == find:
#             check += 1
#         if check == 2:
#             find_index = i
#             break
#
#     return find_index
#
# size = int(input('Введите размер списка: '))
# list = create_string_list(size)
# find = input('Ищем: ')
# if check_double_first_value(list, find) == (-1):
#     print('Нет повторов')
# else:
#     print(f'Искомый элемент стоит на {check_double_first_value(list,find)} позиции.')
