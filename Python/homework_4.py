"""задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

# def list_easy_value(number):
#     list = []
#     for i in range(2, number):
#         check = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 check = 1
#         if check == 0:
#             list.append(i)
#     return list
#
# def find_prime_factors(number, easy_list):
#     list = []
#     for i in easy_list:
#         if number / i == 1:
#             list.append((i))
#             break
#         else:
#             while number % i == 0:
#                 list.append(i)
#                 number /= i
#     return list
#
# try:
#     num = int(input('Введите число N: '))
#     list = find_prime_factors(num, list_easy_value(num))
#     print(f'{num} = ', end='')
#     for i in range(len(list)):
#         if i == len(list) - 1:
#             print(list[i])
#         else:
#             print(f'{list[i]} *', end=' ')
#
# except:
#     print('Введите целое число!')


"""задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности."""

# def create_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(int(input(f'Введите {i + 1} число: ')))
#
#     return lst
#
# try:
#     size = int(input('Введите предварительный размер вашего списка: '))
#     lst = create_list(size)
#     print(f'\nИсходный список: {lst}')
#     new_list = list(set(lst))
#     print(f'\nCписок неповторяющихся элементов: {new_list}')
#
# except:
#     print('Некорректный ввод!')


"""задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""

# import random
#
# def create_string_polynomial(k):
#     sting = ''
#     for i in range(k + 1):
#         random_value = random.randint(0, 100)
#         if random_value != 0:
#             if i == k - 1:
#                 sting += f'({random_value} * x) + '
#             elif i == k:
#                 sting += f'{random_value}'
#             else:
#                 sting += f'({random_value} * x^{k - i}) + '
#     sting += f' = 0'
#     return sting
#
# try:
#     real_k = int(input('Введите натуральную степень k: '))
#     if real_k <= 0:
#         print('Введите натуральное число!')
#         exit()
#
#     result_string = create_string_polynomial(real_k)
#     print(result_string)
#
#     f = open('polynomial.txt', 'a')
#     f.writelines('\n' + result_string)
#     f.close()
#
# except:
#     print('Введите натуральное число!')


"""задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. 
например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, 
сделать обработку исключений."""

# def string_to_value(user_string):
#     string_list = user_string.split('x')
#     values = []
#     first_value = 0
#     if user_string[0] == 'x':
#         values.app+end(1)
#         first_value = 1
#     elif user_string[0:2] == '-x':
#         values.append(-1)
#         first_value = 1
#     minus = 0
#     check = 0
#     for i in range(first_value, len(string_list)):
#         for w in string_list[i]:
#             if w.isdigit():
#                 if check != 1:
#                     if minus == 1:
#                         values.append(int(w) * (-1))
#                         minus = 0
#                         break
#                     else:
#                         values.append(int(w))
#                         break
#                 else:
#                     check = 0
#             elif w == '-':
#                 minus = 1
#             elif w == '^':
#                 check = 1
#     return values
#
# def quadratic_equation(abc_list):
#     d = abc_list[1] ** 2 - 4 * abc_list[0] * abc_list[2]
#     x = []
#     if d > 0:
#         x.append((((-1) * abc_list[1]) + d ** 0.5) / (2 * abc_list[0]))
#         x.append((((-1) * abc_list[1]) - d ** 0.5) / (2 * abc_list[0]))
#     elif d == 0:
#         x.append(((-1) * abc_list[1] / (2 * abc_list[0])))
#
#     return x
#
# try:
#     user = input('Введите квадратное уравнение типа "a*x^2+b*x+6=0": ')
#     user_string = user.replace('х', 'x', 2)
#     values_list = string_to_value(user_string)
#     x = quadratic_equation(values_list)
#     if len(x) > 0:
#         print('Корни уравнения: ')
#         for i in x:
#             print(f'x = {i}')
#     else:
#         print('Корней нет')
#
# except:
#     print('Введите квадратное уравнение типа "a*x^2+b*x+6=0"!')


"""задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. 
Тема чат-бота любая. Просьба - постараться не использовать простой одномерный список или простой одномерный словарь."""

import json

def save(name, pr):
    with open(f'{name}.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(pr, ensure_ascii=False))

def load(name, pr):
    with open(f'{name}.json', 'r', encoding='utf-8') as fh:
        pr = json.load(fh)
    print('Загруза успешна!')
    return pr

def show_keys(dict):
    result = ''
    count = 0
    for i in dict.keys():
        if count < len(dict) - 1:
            result += i + ', '
            count += 1
        else:
            result += i

    return result

def show_dict(dict):
    result = ''
    for i in dict.keys():
        result += f'{i}: {dict[i]}\n'

    return result


users = {}
items = []

try:
    print('Привет! Данный бот предназначен для учета складских позиций. \nЗагружаем базу данных...')
    users = load('users', users)

except:
    print('Ваша база данных пуста. Начнем работу?)')


while True:
    command = input('Введите команду: ')
    if command == '/help':
        print(f'/help - помощь'
              f'\n/adduser - добавить нового клиента'
              f'\n/additem - добавить новый товар клиенту'
              f'\n/showusers - отобразить список пользователей склада'
              f'\n/showitems - отобразить список товаров клиента'
              f'\n/saveusers - сохранить базу данных с клиентами'
              f'\n/loadusers - загрузить базу данных с клиентами'
              f'\n/removeuser - удалить клиента'
              f'\n/removeitem - удалить товар'
              f'\n/showall - показать склад'
              f'\n/stop - остановить бота\n')

    elif command == '/adduser':
        name = input('Введите имя: ')
        if name in users.keys():
            answer = input(f'Клиент с таким именем уже есть. \nНазвать {name}' + '1? (да, нет) ')
            if answer == 'да' or answer == 'Да':
                name += '1'
                users[name] = []
                save('users', users)
                print('Клиент успешно добавлен\n')
            else:
                print('Не удаловь добавить нового клиента\n')
        else:
            users[name] = []
            save('users', users)
            print('Клиент успешно добавлен\n')

    elif command == '/additem':
        name = input('Введите имя, кому вы хотите добавить товар: ')
        if name in users.keys():
            items = users[name]
            items.append(input('Введите наименование товара: '))
            users[name] = items
            save('users', users)
            print('Товар успешно добавлен\n')
        else:
            print('Такого имени нет в базе данных!\n')

    elif command == '/showusers':
        print(f'Список пользователей склада: \n{show_keys(users)}\n')

    elif command == '/showitems':
        name = input('Введите имя клиента: ')
        if name in users.keys():
            print(users[name])
        else:
            print('Такого имени нет в базе данных!\n')

    elif command == '/saveusers':
        save('users', users)

    elif command == '/loadusers':
        users = load('users', users)

    elif command == '/stop':
        save('users', users)
        exit('До свидания!')

    elif command == '/removeuser':
        name = input('Введите имя клиента, которого хотите удалить: ')
        if name in users.keys():
            del users[name]
            save('users', users)
            print('Клиент успешно удален\n')
        else:
            print('Такого имени нет в базе данных!\n')

    elif command == '/removeitem':
        name = input('Введите имя клиента, у которого хотите удалить товарь: ')
        if name in users.keys():
            items = users[name]
            print(items)
            item = input('Введите товар, который хотите удалить: ')
            if item in items:
                items.remove(item)
                users[name] = items
                save('users', users)
                print('Клиент успешно удален\n')
            else:
                print('Такого товара нет!')
        else:
            print('Такого имени нет в базе данных!\n')

    elif command == '/showall':
        print(f'Ваш склад:\n{show_dict(users)}')

    else:
        print('Неопознанная команда. Воспользуйтесь /help\n')





