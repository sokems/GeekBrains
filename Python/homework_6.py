"""Задача 1. Создайте программу для игры в "Крестики-нолики"."""

# import random
#
# def create_field():
#     field = [[' ' for i in range(3)] for j in range(3)]
#     return field
#
# def show_field(array):
#     print('———————————————————')
#     for i in range(len(array)):
#         str = '|'
#         for j in range(len(array[i])):
#             str += '  ' + array[i][j] + '  |'
#         print(str)
#         print('———————————————————')
#
# def check_win(array, str_player):
#     check = 0
#     if (array[0][0] == str_player and array[0][1] == str_player and array[0][2] == str_player) or \
#             (array[1][0] == str_player and array[1][1] == str_player and array[1][2] == str_player) or \
#             (array[2][0] == str_player and array[2][1] == str_player and array[2][2] == str_player) or \
#             (array[0][0] == str_player and array[1][0] == str_player and array[2][0] == str_player) or \
#             (array[0][1] == str_player and array[1][1] == str_player and array[2][1] == str_player) or \
#             (array[0][2] == str_player and array[1][2] == str_player and array[2][2] == str_player) or \
#             (array[0][0] == str_player and array[1][1] == str_player and array[2][2] == str_player) or \
#             (array[0][2] == str_player and array[1][1] == str_player and array[2][0] == str_player):
#         print(f'Победил игрок, который ходил "{str_player}"!')
#         check = 1
#     return check
#
# field = create_field()
# show_field(field)
# print('Поиграем?\n')
# player = random.randint(1, 2)
# str_player = ' '
# if player == 1:
#     print('Первым ходит игрок!')
#     str_user = 'X'
#     str_bot = 'O'
# else:
#     print('Первым ходит компьютер!')
#     str_user = 'O'
#     str_bot = 'X'
#
# try:
#     while True:
#         if player == 1:
#             print('Ходит игрок!')
#             str_player = str_user
#             while True:
#                 row = int(input('Введите номер строки: '))
#                 column = int(input('Введите номер столбца: '))
#                 if field[row - 1][column - 1] == ' ':
#                     field[row - 1][column - 1] = str_user
#                     break
#                 else:
#                     print('Данная ячейка уже занята!\n')
#             show_field(field)
#             player = 0
#         else:
#             print('Ходит компьютер!')
#             str_player = str_bot
#             while True:
#                 row = random.randint(1, 3)
#                 column = random.randint(1, 3)
#                 if field[row - 1][column - 1] == ' ':
#                     field[row - 1][column - 1] = str_bot
#                     break
#                 else:
#                     print('Данная ячейка уже занята!\n')
#             show_field(field)
#             player = 1
#
#         if check_win(field, str_player) == 1:
#             break
#         else:
#             print('—————————————————————————————————————————————————————————')
#
# except:
#     print('Некорректный ввод!')

"""Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
приоритет операций стандартный.

-Добавьте возможность использования скобок, меняющих приоритет операций."""

def convert_str_to_digit(str_user):
    str_digit = str_user.replace(' ', '')
    if str_digit[0] == '-':
        str_digit = '0' + str_digit
    str_digit = str_digit.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ')
    list_digit = str_digit.split(' ')

    for i in range(len(list_digit)):
        list_digit[i] = int(list_digit[i])

    return list_digit

def create_list_operations(str_user):
    str_oper = str_user.replace(' ', '')
    list_oper = []
    for i in str_oper:
        if i.isdigit():
            i = ' '
        else:
            list_oper.append(i)

    return list_oper

def solution_example(list_digit, list_oper):
    for n in range(len(list_digit)):
        for i in range(len(list_oper)):
            if list_oper[i] == '*':
                list_digit[i] *= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break

        for i in range(len(list_oper)):
            if list_oper[i] == '/':
                list_digit[i] /= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break

        for i in range(len(list_oper)):
            if list_oper[i] == '+' or list_oper[i] == '-':
                if list_oper[i] == '+':
                    list_digit[i] += list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                    break
                elif list_oper[i] == '-':
                    list_digit[i] -= list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                    break

    return list_digit

def remove_bracketed_expression(str_user):
    bracketed_expression = ''
    start_index = 0
    end_index = 0
    check = 1
    str_new = ''
    for i in range(len(str_user)):
        if str_user[i] == '(':
            start_index = i + 1
            check = 0
        elif str_user[i - 1] == ')':
            end_index = i - 1
            check = 1
        if check == 1:
            str_new += str_user[i]

    bracketed_expression = str_user[start_index:end_index]
    bracketed_expression_digit = convert_str_to_digit(bracketed_expression)
    bracketed_expression_oper = create_list_operations(bracketed_expression)
    result = solution_example(bracketed_expression_digit, bracketed_expression_oper)
    str_new += str(result[0])
    return str_new


str_user = input('Введите пример: ')
if '(' and ')' in str_user:
    str_user = remove_bracketed_expression(str_user)
list_digit = convert_str_to_digit(str_user)
list_oper = create_list_operations(str_user)
result = solution_example(list_digit, list_oper)
print(f'{str_user} = {result[0]}')


"""Задача FOOTBALL необязательная: Напишите программу, которая принимает на стандартный вход список игр футбольных 
команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6"""