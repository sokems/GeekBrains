"""Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата."""

num = int(input('Введите целое число: '))
list_hex = []
list_hex_res = []

while True:
    if num < 16:
        list_hex.insert(0, num)
        break
    list_hex.insert(0, num % 16)
    num //= 16

for value in list_hex:
    if value == 10:
        value = 'A'
    elif value == 11:
        value = 'B'
    elif value == 12:
        value = 'C'
    elif value == 13:
        value = 'D'
    elif value == 14:
        value = 'E'
    elif value == 15:
        value = 'F'

    list_hex_res.append(value)

num_hex = ''.join(str(x) for x in list_hex_res)

print(f'Шестнадцатиричное представление - {num_hex}')