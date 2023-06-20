"""Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions."""

def sum_of_fractions(frac_1, frac_2):
    sum_numerator = int(frac_1[0]) * int(frac_2[1]) + int(frac_2[0]) * int(frac_1[1])
    sum_denominator = int(frac_1[1]) * int(frac_2[1])
    return [sum_numerator, sum_denominator]

def multi_of_fractions(frac_1, frac_2):
    multi_numerator = int(frac_1[0]) * int(frac_2[0])
    multi_denominator = int(frac_1[1]) * int(frac_2[1])
    return [multi_numerator, multi_denominator]

num_1 = input('Введите 1 дробь вида “a/b”: ')
num_2 = input('Введите 2 дробь вида “a/b”: ')

list_num_1 = num_1.split('/')
list_num_2 = num_2.split('/')

list_res_sum = sum_of_fractions(list_num_1, list_num_2)
list_res_multi = multi_of_fractions(list_num_1, list_num_2)

print(f'Сумма дробей: {list_res_sum[0]}/{list_res_sum[1]}')
print(f'Произведение дробей: {list_res_multi[0]}/{list_res_multi[1]}')



