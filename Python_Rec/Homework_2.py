"""
Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
"""

list_1 = [2, 5, 8, 2, 12, 12, 4]
list_2 = [2, 7, 12, 3]

for value in list_1[:]:
    if value in list_2:
        list_1.remove(value)

print(list_1)

"""
Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например: 
второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
"""

dict_day = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое'
}

dict_mounth = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

message = input('Введите дату в формате dd.mm.yyyy: ')
day = dict_day[message[0:2]]
mounth = dict_mounth[message[3:5]]
year = message[6:10]
if(message[2] == '.') and (message[5] == '.'):
    print('{} {} {} года'.format(day, mounth, year))
else:
    print('Ввели неверную дату!')

"""
Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
"""

list = [2, 2, 5, 12, 8, 2, 12]
new_list = []

for value in list:
    if list.count(value) == 1:
        new_list.append(value)

print(new_list)