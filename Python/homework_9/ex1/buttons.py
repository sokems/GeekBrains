import calc
import log

def button_calc(str_user):
    try:
        list_digit = calc.convert_str_to_digit(str_user)
        list_oper = calc.create_list_operations(str_user)
        result = calc.solution_example(list_digit, list_oper)
        log.logger(str_user, result[0])
        res_text = f'{str_user} = {result[0]}'
    except:
        if str_user == None:
            pass
        else:
            log.logger_err(str_user, 'Ошибка ввода')
            res_text = 'Ошибка ввода!'

    return res_text

def button_calc_comp(str_user):
    try:
        j = (-1)**(1/2)
        result = eval(str_user)
        log.logger(str_user, result)
        res_text = f'{str_user} = {result}'
    except:
        if str_user == None:
            pass
        else:
            log.logger_err(str_user, 'Ошибка ввода')
            res_text = 'Ошибка ввода!'

    return res_text

