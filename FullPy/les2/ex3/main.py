"""✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой."""

import decimal

d = decimal.Decimal(input('Введите диаметр: '))
pi = decimal.Decimal(3.141_592_653_589_793_238_462_643_383_279_502_884_197_169)

if 0 < d <= 1000:
    decimal.getcontext().prec = 42
    len_round = 2 * pi * decimal.Decimal(d / 2)
    s = 2 * pi * ((d / 2) ** 2)
    print(len_round)
    print(s)

else:
    print('Введите число в диапазоне от 0 до 1001')