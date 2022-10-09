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
"""
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



