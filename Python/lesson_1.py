"""
1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
"""

# try:
#     num_1 = int(input('Введите 1 число: '))
#     num_2 = int(input('Введите 2 число: '))
#     if num_1 ** 2 == num_2:
#         print(f'Второе число является квадратом первого.')
#     elif num_2 ** 2 == num_1:
#         print(f'Первое число является квадратом второго.')
#     else:
#         print(f'Ниодно число не является квадратом другого.')
# except:
#     print('Введите целое число.')

"""
2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них, минимальное, их индексы, средне-
арифметическое, медианное.
"""

numbers = []
size = 4

for i in range(size):
    number = float(input(f'Введите {i + 1} число: '))
    numbers.append(number)

index_max = 0
i = 1
for i in range(len(numbers)):
    if numbers[i] > numbers[index_max]:
        index_max = i

print(f'Максимальный элемент равен {numbers[index_max]}, а его индекс равен {index_max}')

index_min = 0
j = 1
for j in range(len(numbers)):
    if numbers[j] < numbers[index_min]:
        index_min = j

print(f'Минимальный элемент равен {numbers[index_min]}, а его индекс равен {index_min}')

sum = 0
for k in range(len(numbers)):
    sum += numbers[k]

mid_sum = sum / len(numbers)
print(f'Среднее арифметическое равно {mid_sum}')

l = 1

def sort_up(list):
    new_list = list
    for n in range(len(list)):
        for l in range(len(list)):
            if list[n] < list[l]:
                temp = new_list[n]
                new_list[n] = new_list[l]
                new_list[l] = temp
    return new_list

new_numbers = sort_up(numbers)
if len(new_numbers) % 2 == 0:
    middle_number = (new_numbers[len(new_numbers) // 2 - 1] + new_numbers[len(new_numbers) // 2]) / 2
else:
    middle_number = new_numbers[len(new_numbers) // 2]

print(f'Упорядоченный массив: {new_numbers}.\nМедиана равна {middle_number}')