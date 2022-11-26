def convert_str_to_digit(str_user):
    str_digit = str_user.replace(' ', '')
    if str_digit[0] == '-':
        str_digit = '0' + str_digit
    str_digit = str_digit.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ')
    list_digit = str_digit.split(' ')

    for i in range(len(list_digit)):
        list_digit[i] = int(list_digit[i])

    return list_digit

def create_list_operations(str_user):
    str_oper = str_user.replace(' ', '')
    list_oper = []
    for i in str_oper:
        if i.isdigit():
            i = ' '
        else:
            list_oper.append(i)

    return list_oper

def solution_example(list_digit, list_oper):
    for n in range(len(list_digit)):
        for i in range(len(list_oper)):
            if list_oper[i] == '*':
                list_digit[i] *= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break

        for i in range(len(list_oper)):
            if list_oper[i] == '/':
                list_digit[i] /= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break

        for i in range(len(list_oper)):
            if list_oper[i] == '+' or list_oper[i] == '-':
                if list_oper[i] == '+':
                    list_digit[i] += list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                    break
                elif list_oper[i] == '-':
                    list_digit[i] -= list_digit[i + 1]
                    del list_digit[i + 1]
                    del list_oper[i]
                    break

    return list_digit


