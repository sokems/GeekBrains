"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

# try:
#     day = int(input("Введите цифру дня недели: "))
#     if (day == 6) or (day == 7):
#         print('Введенный день является выходным.')
#     else:
#         print('Введенный день - будни.')
# except:
#     print('Введите целое число')
"""

"""
Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def convert_value_to_bool(num):
    if num == 1:
        return True
    elif num == 0:
        return False

check = 0

for x in range(2):
    for y in range(2):
        for z in range(2):
            pred_x = convert_value_to_bool(x)
            pred_y = convert_value_to_bool(y)
            pred_z = convert_value_to_bool(z)

            left = not (pred_x or pred_y or pred_z)
            right = not (pred_x) and not (pred_y) and not (pred_z)

            if (left != right):
                check = 1
                break

if check == 0:
    print('Удтверждение истинно.')
else:
    print('Удтверждение ложно.')
"""

"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
плоскости, в которой находится эта точка (или на какой оси она находится).


def how_quarters(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print('Точка находится в 1 четверти.')
        elif x < 0 and y > 0:
            print('Точка находится во 2 четверти.')
        elif x < 0 and y < 0:
            print('Точка находится в 3 четверти.')
        else:
            print('Точка находится в 4 четверти.')
    elif x == 0 and y == 0:
        print('Х и У не могут быть одновременно равны 0 по условию задачи.')
    elif x == 0:
        print('Точка находить на оси координат Y.')
    else:
        print('Точка находить на оси координат X.')

x_coord = float(input('Введите координату Х точки: '))
y_coord = float(input('Введите координату Y точки: '))

how_quarters(x_coord, y_coord)
"""

"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти
(x и y).

try:
    def how_coordinates(num):
        if num == 1:
            print('X > 0, Y > 0')
        elif num == 2:
            print('X < 0, Y > 0')
        elif num == 3:
            print('X < 0, Y < 0')
        elif num == 4:
            print('X > 0, Y > 0')
        else:
            print('Такой четверти не существует')

    number_quarters = int(input('Введите номер четверти: '))
    how_coordinates(number_quarters)

except:
    print('Введите целое число!')
"""

"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def distance_between_points(x1, y1, x2, y2):
    cathet_first = y1 - y2
    cathet_second = x1 - x2
    distance = (cathet_first ** 2 + cathet_second ** 2) ** 0.5
    return distance

x_coord_first = float(input('Введите координату Х первой точки: '))
y_coord_first = float(input('Введите координату Y первой точки: '))
x_coord_second = float(input('Введите координату Х второй точки: '))
y_coord_second = float(input('Введите координату Y второй точки: '))

print(f'Расстояние между точками ({x_coord_first}; {y_coord_first}) и ({x_coord_second}; {y_coord_second}) '
      f'равно {round(distance_between_points(x_coord_first, y_coord_first, x_coord_second, y_coord_second), 3)}')
"""

"""
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число 
и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит 
результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

try:
    def oper_plus(num_1, num_2):
        return num_1 + num_2

    def oper_minus(num_1, num_2):
        return num_1 - num_2

    def oper_div(num_1, num_2):
        if num_2 != 0:
            return num_1 / num_2
        else:
            return 'Деление на 0!'

    def oper_multi(num_1, num_2):
        return num_1 * num_2

    def oper_mod(num_1, num_2):
        return num_1 % num_2

    def oper_pow(num_1, num_2):
        return num_1 ** num_2

    def oper_int_div(num_1, num_2):
        if num_2 != 0:
            return num_1 // num_2
        else:
            return 'Деление на 0!'

    number_1 = float(input('Введите первое число: '))
    operation = input('Введите операцию над числами: ')
    number_2 = float(input('Введите второе число: '))

    if operation == '+':
        result = oper_plus(number_1, number_2)
    elif operation == '-':
        result = oper_minus(number_1, number_2)
    elif operation == '/':
        result = oper_div(number_1, number_2)
    elif operation == '*':
        result = oper_multi(number_1, number_2)
    elif operation == 'mod':
        result = oper_mod(number_1, number_2)
    elif operation == 'pow':
        result = oper_pow(number_1, number_2)
    elif operation == 'div':
        result = oper_int_div(number_1, number_2)

    print(f'\n{number_1} {operation} {number_2} = {result}')

except:
    print('Некорректный ввод!')
"""

"""
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
Отсортировать элементы по возрастанию слева направо и сверху вниз.
"""

def create_2d_array(row, column):
    array = [[(int(input(f'Введите число с индексами ({i}: {j}): '))) for i in range(column)] for j in range(row)]
    return array

def sort_2d_array(array):
    new_array = []
    for i in range(len(array[0])):
        for j in range(len(array)):
            new_array.append(array[i][j])

    k = 0
    while k < len(new_array) - 1:
        if new_array[k] > new_array[k + 1]:
            temp = new_array[k]
            new_array[k] = new_array[k + 1]
            new_array[k + 1] = temp
            k = 0
        else:
            k += 1

    n = 0
    for r in range(len(array[0])):
        for c in range(len(array)):
            array[r][c] = new_array[n]
            n += 1

    return array

row = int(input('Введите количество строк в массиве: '))
column = int(input('Введите количество столбцов в массиве: '))
array = create_2d_array(row, column)

print(f'Изначальный массив: {array}.\nОтсортированный массив: {sort_2d_array(array)}.')