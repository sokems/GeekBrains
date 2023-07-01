"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""


def tuple_path(data):
    res_tuple = []
    find_index = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] == '/':
            res_tuple.append(data[0:i + 1])
            break

    for i in range(len(data)):
        if data[i] == '/':
            find_index = i
        if data[i] == '.':
            res_tuple.append(data[find_index + 1:i])
            res_tuple.append(data[i + 1:len(data)])
            break

    return res_tuple

data = 'C:/user/sokem/data.bat'

print(tuple_path(data))