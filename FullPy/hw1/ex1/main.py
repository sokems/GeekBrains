"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным
или равносторонним."""

first_side = float(input('Введите первую сторону треугольника: '))
second_side = float(input('Введите вторую сторону треугольника: '))
third_side = float(input('Введите третью сторону треугольника: '))

if (first_side + second_side) > third_side \
        and (first_side + third_side) > second_side \
        and (third_side + second_side) > first_side:
    if (first_side == second_side == third_side):
        print('Треугольник равносторонний')
    elif (first_side == second_side) or (second_side == third_side) or (first_side == third_side):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует!')