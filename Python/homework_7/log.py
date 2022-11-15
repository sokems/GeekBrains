from datetime import datetime as dt

def logger(data_start, res):
    time = dt.now().strftime('%H:%M')
    with open('logs.txt', 'a') as file:
        file.write(f'{time}, пользователь ввел {data_start}, ответ {res}\n')

def logger_err(data_start, res):
    time = dt.now().strftime('%H:%M')
    with open('logs.txt', 'a') as file:
        file.write(f'{time}, пользователь ввел {data_start}, {res}\n')

def logger_start():
    time = dt.now().strftime('%H:%M')
    with open('logs.txt', 'a') as file:
        file.write(f'{time}, пользователь запустил программу\n')

def logger_exit():
    time = dt.now().strftime('%H:%M')
    with open('logs.txt', 'a') as file:
        file.write(f'{time}, пользователь закрыл программу\n')
