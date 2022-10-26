"""задача 1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
конкурента?
Делаем игру против бота
а) Подумайте как наделить бота интеллектом"""

# import random
#
# count = 2021
# person = random.randint(1, 2)
# print('Играем против бота!')
#
# while count != 0:
#     if person == 1:
#         print('Ходит игрок')
#         write_value = int(input('Сколько конфет вы заберете? '))
#         while write_value < 1 or write_value > 28 or write_value > count:
#             if count > 28:
#                 write_value = int(input('Можно взять не больше 28 конфет! Сколько конфет вы заберете? '))
#             else:
#                 write_value = int(input(f'Можно взять не больше {count} конфет! Сколько конфет вы заберете? '))
#         count -= write_value
#         person = 0
#         print(f'Осталось {count} конфет!\n')
#     else:
#         print('Ходит бот')
#         if count < 29:
#             write_value = count
#         elif count < 57:
#             write_value = count - 29
#         else:
#             write_value = random.randint(1, 28)
#         print(f'Бот взял конфет в количестве {write_value}')
#         count -= write_value
#         person = 1
#         print(f'Осталось {count} конфет!\n')
#
# if person == 0:
#     print('Победил игрок!')
# else:
#     print('Победил бот!')


"""задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах."""

# def open_file(name):
#     try:
#         r = open(f'{name}.txt', 'r')
#         values = r.readlines()
#         r.close()
#         value = values[0]
#         print(f'Из файла импортируем последовательность: \n{value}\n')
#         return value
#     except:
#         exit('Некорректное имя файла!')
#
# def compresion(value):
#     i = 0
#     res = ''
#     value += ' '
#
#     while value[i] != ' ':
#         count = 1
#         while value[i] == value[i + 1]:
#             count += 1
#             i += 1
#         else:
#             res += str(count) + str(value[i]) + ' '
#             i += 1
#
#     print(f'Сжатая последовательность:\n{res}')
#     return res
#
# def rebuild(value):
#     res = ''
#     values = value.split(' ')
#     for i in range(len(values)):
#         main_value = values[i][-1]
#         l = len(values[i]) - 1
#         count_value = int(values[i][:l])
#         res += main_value * count_value
#
#     print(f'Восстановленная последовательность:\n{res}')
#     return res
#
#
# name = input('Введите название файла (без расширения): ')
# value = open_file(name)
#
# try:
#     press = int(input('Что вы хотите сделать?\n1. Сжать\n2. Восстановить\n'))
#     if press == 1:
#         res = compresion(value)
#     elif press == 2:
#         res = rebuild(value)
#
#     w = open('result.txt', 'w')
#     w.writelines(res)
#     w.close()
#
# except:
#     print('Выберите действие. 1 или 2.')


"""задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя."""

# def delete_word(word, text):
#     text_list = text.split(' ')
#     count = 0
#     res = ''
#     res_list = []
#     check = 0
#     for word in text_list:
#         for letter in range(len(word)):
#             if (word[letter] == 'а') and (word[letter + 1] == 'б') and (word[letter + 2] == 'в'):
#                 check = 1
#                 break
#         if check == 0:
#             res_list.append(word)
#         else:
#             check = 0
#
#     for i in res_list:
#         res += i + ' '
#
#     return res
#
#
# r = open('text.txt', 'r', encoding='utf-8')
# values = r.readlines()
# r.close()
# value = values[0]
# print(f'Из файла импортируем текст: \n{value}\n')
# word = 'абв'
#
# result = delete_word(word, value)
# print(f'Из текста удалили все слова с "{word}". Результат: \n{result}')


"""задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9"""

# def max_degree(poly):
#     list = poly.replace(' ', '').split('x')
#     degree = 0
#     check = 0
#     for i in list:
#         for l in range(len(i)):
#             if i[l] == '^':
#                 check = 1
#                 degree = int(i[l + 1])
#                 break
#         if check == 1:
#             check = 0
#             break
#     return degree
#
# def list_of_coefficients(poly1, degree):
#     list = poly1.split('+')
#     new_list = []
#     d = degree
#     i = 0
#     while d > 0:
#         if i < len(list):
#             if not 'x' in list[i]:
#                 new_list.append(0)
#             else:
#                 if list[i][0] == '-':
#                     if list[i][1].isdigit():
#                         temp = int(list[i][1]) * (-1)
#                     elif list[i][1] == 'x':
#                         temp = -1
#                 elif list[i][0].isdigit():
#                     temp = int(list[i][0])
#                 elif list[i][0] == 'x':
#                     temp = 1
#                 for l in range(len(list[i])):
#                     if list[i][l] == 'x':
#                         if ('^' in list[i]) and (list[i][l + 1] == '^'):
#                             if list[i][l + 2] == str(d):
#                                 new_list.append(temp)
#                                 i += 1
#                             else:
#                                 new_list.append(0)
#                             break
#                         else:
#                             if '1' == str(d):
#                                 new_list.append(temp)
#                                 i += 1
#                             else:
#                                 new_list.append(0)
#                             break
#         else:
#             new_list.append(0)
#             new_list.append(0)
#         d -= 1
#     for j in list:
#         if not 'x' in j:
#             new_list.append(int(j))
#     return new_list
#
# def list_to_polynomial(list1):
#     res = ''
#     degree = len(list1) - 1
#     for i in list1:
#         if i != 0:
#             if degree == 1:
#                 res += f'{str(i)}*x^{degree} + '
#                 degree -= 1
#             elif degree == 0:
#                 res += f'{str(i)}'
#             else:
#                 res += f'{str(i)}*x^{degree} + '
#                 degree -= 1
#         else:
#             degree -= 1
#
#     res = res.replace('+ -', '- ')
#     print(res)
#
#
# polynomial_first = ' 2*x^4 + 6'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')
# polynomial_second = ' 9*x^2 - 9'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')
# degree1 = max_degree(polynomial_first)
# degree2 = max_degree(polynomial_second)
# maximum_degree = max(degree1, degree2)
# list1 = list_of_coefficients(polynomial_first, maximum_degree)
# list2 = list_of_coefficients(polynomial_second, maximum_degree)
# res_list = [x + y for x, y in zip(list1, list2)]
# list_to_polynomial(res_list)

"""задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную 
возрастающую последовательность. Порядок элементов менять нельзя.

*Пример:* 
[1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
[1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]"""

def max_sequence(list1):
    list1 = list(set(list1))
    res_list = []
    new_list = []
    while len(list1) > 0:
        min_value = min(list1)
        list1.remove(min_value)
        while True:
            new_list.append(min_value)
            min_value += 1
            if not (min_value in list1):
                if len(new_list) > len(res_list):
                    res_list = new_list.copy()
                    new_list = []
                break
            list1.remove(min_value)
    return res_list

def create_list(size):
    lst = []
    for i in range(size):
        lst.append(int(input(f'Введите {i + 1} число: ')))
    print(f'\nВаш список: {lst}')
    return lst

size = int(input('Введите размер списка: '))
user_list = create_list(size)

print(f'\nМаксимальная последовательность вашего списка: {max_sequence(user_list)}')