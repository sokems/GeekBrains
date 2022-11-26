import telebot
from telebot import types
import game
import random

token = '5929548344:AAFYDzBKJq7svkUhxS68jdmOBSXQUNHVdNA'
bot = telebot.TeleBot(token)
field = []
player = 0
str_player = ' '
str_bot = ' '
str_user = ' '
again = 0

@bot.message_handler(commands=['start'])
def start_message(message):
    global field
    global player
    global new_game
    global str_bot
    global str_player
    global str_user
    field = game.create_field()
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>!', parse_mode='html')
    bot.send_message(message.chat.id, game.show_field(field))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    again_game = types.KeyboardButton('Начать')
    markup.add(again_game)
    bot.send_message(message.chat.id, 'Сыграем в крестики нолики?', reply_markup=markup)


@bot.message_handler(content_types='text')
def text_message(message):
    global field
    global player
    global new_game
    global str_bot
    global str_player
    global str_user
    global again
    try:
        if message.text == 'Начать':
            if again == 1:
                bot.send_message(message.chat.id, 'Начинаем заново!')
            again = 1
            player = random.randint(1, 2)
            if player == 1:
                bot.send_message(message.chat.id, 'Первым ходит игрок!')
                bot.send_message(message.chat.id, 'Введите номер строки и столбца (1 2)')
                str_user = 'X'
                str_bot = 'O'
                str_player = str_user
                text = message.text
                bot.send_message(message.chat.id, text)
                if field[int(text[0]) - 1][int(text[2]) - 1] == ' ':
                    field[int(text[0]) - 1][int(text[2]) - 1] = str_user
                    bot.send_message(message.chat.id, game.show_field(field))
                    player = 0
                else:
                    bot.send_message(message.chat.id, 'Данная ячейка уже занята!')
            else:
                bot.send_message(message.chat.id, 'Первым ходит бот!')
                str_user = 'O'
                str_bot = 'X'
                field = game.walk_bot(str_player, str_bot, field)
                bot.send_message(message.chat.id, game.show_field(field))
                player = 1
                bot.send_message(message.chat.id, 'Ходит игрок!')
                bot.send_message(message.chat.id, 'Введите номер строки и столбца (1 2)')
        else:
            if player == 1:
                str_player = str_user
                text = message.text
                bot.send_message(message.chat.id, text)
                if field[int(text[0]) - 1][int(text[2]) - 1] == ' ':
                    field[int(text[0]) - 1][int(text[2]) - 1] = str_user
                    bot.send_message(message.chat.id, game.show_field(field))
                    player = 0
                    bot.send_message(message.chat.id, 'Продолжаем?')
                else:
                    bot.send_message(message.chat.id, 'Данная ячейка уже занята!')
                    bot.send_message(message.chat.id, 'Введите номер строки и столбца (1 2)')
            elif player == 0:
                bot.send_message(message.chat.id, 'Ходит бот!')
                field = game.walk_bot(str_player, str_bot, field)
                bot.send_message(message.chat.id, game.show_field(field))
                player = 1
                bot.send_message(message.chat.id, 'Ходит игрок!')
                bot.send_message(message.chat.id, 'Введите номер строки и столбца (1 2)')
            if game.check_win(field, str_player) == 1:
                bot.send_message(message.chat.id, f'Победил игрок, который ходил "{str_player}"!')
                field = game.create_field()
                bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}, начнем заново?</b>!', parse_mode='html')
                bot.send_message(message.chat.id, game.show_field(field))
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                again_game = types.KeyboardButton('Начать')
                markup.add(again_game)
    except:
        bot.send_message(message.chat.id, 'Я Вас не понял(')


bot.polling(none_stop=True)

