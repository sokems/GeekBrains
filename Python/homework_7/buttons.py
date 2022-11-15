import calc
import log
import easygui

def button_calc():
    try:
        str_user = easygui.enterbox(msg='Введите пример', title='Калькулятор')
        list_digit = calc.convert_str_to_digit(str_user)
        list_oper = calc.create_list_operations(str_user)
        result = calc.solution_example(list_digit, list_oper)
        log.logger(str_user, result[0])
        easygui.msgbox(msg=f'{str_user} = {result[0]}', title='Ответ')
    except:
        if str_user == None:
            pass
        else:
            log.logger_err(str_user, 'Ошибка ввода')
            easygui.msgbox(msg='Ошибка ввода!', title='Ответ')

def button_log():
    with open('logs.txt') as file:
        text = file.read()
    easygui.textbox('История операций', 'Калькулятор', text)

