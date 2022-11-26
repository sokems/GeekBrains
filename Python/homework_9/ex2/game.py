import random

def create_field():
    field = [[' ' for i in range(3)] for j in range(3)]
    return field

def show_field(array):
    str = '——————\n'
    for i in range(len(array)):
        str += '|'
        for j in range(len(array[i])):
            str += '  ' + array[i][j] + '  |'
        str += '\n'
        str += '——————\n'
    return str

def walk_bot(str_player, str_bot, field):
    str_player = str_bot
    while True:
        row = random.randint(1, 3)
        column = random.randint(1, 3)
        if field[row - 1][column - 1] == ' ':
            field[row - 1][column - 1] = str_bot
            break
    return field

def check_win(array, str_player):
    check = 0
    if (array[0][0] == str_player and array[0][1] == str_player and array[0][2] == str_player) or \
            (array[1][0] == str_player and array[1][1] == str_player and array[1][2] == str_player) or \
            (array[2][0] == str_player and array[2][1] == str_player and array[2][2] == str_player) or \
            (array[0][0] == str_player and array[1][0] == str_player and array[2][0] == str_player) or \
            (array[0][1] == str_player and array[1][1] == str_player and array[2][1] == str_player) or \
            (array[0][2] == str_player and array[1][2] == str_player and array[2][2] == str_player) or \
            (array[0][0] == str_player and array[1][1] == str_player and array[2][2] == str_player) or \
            (array[0][2] == str_player and array[1][1] == str_player and array[2][0] == str_player):
        check = 1
    return check
