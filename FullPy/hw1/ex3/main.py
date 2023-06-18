"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
'больше' или 'меньше' после каждой попытки."""

from random import randint

num = randint(0, 1000)
count = 1

while count <= 10:
    count += 1
    user_num = int(input('Введите число: '))

    if user_num == num:
        print('Вы угадали!')
        break

    elif num > user_num:
        print('Больше...')

    elif num < user_num:
        print('Меньше...')

    if count == 11:
        print('Вы не угадали!(((((')

