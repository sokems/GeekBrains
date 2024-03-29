"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

num = int(input('Введите число от 0 до 100.000: '))
check = True

if 100000 >= int(num) >= 0:
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            check = False
    if check:
        print(f'Вы ввели простое число!')
    else:
        print(f'Вы ввели составное число!')
else:
    raise ValueError('Число может быть только в диапазоне от 0 до 100.000')