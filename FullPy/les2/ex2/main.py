"""✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно"""

num = int(input('Введите целое число: '))
list_bin = []
list_oct = []

num_2 = num
while True:
    if num_2 == 1:
        list_bin.insert(0, num_2)
        break
    list_bin.insert(0, num_2 % 2)
    num_2 //= 2

num_2 = num
while True:
    if num_2 < 8:
        list_oct.insert(0, num_2)
        break
    list_oct.insert(0, num_2 % 8)
    num_2 //= 8



num_bin = ''.join(str(x) for x in list_bin)
num_oct = ''.join(str(x) for x in list_oct)

print(f'Двоичное представление - {num_bin}')
print(f'Восьмиричное представление - {num_oct}')