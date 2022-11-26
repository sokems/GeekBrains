import telebot
from telebot import types
import buttons
import log

token = '5928069306:AAGei9Mpu3ZZzFEvC7JAKY6pU_tNS0tzVL0'
bot = telebot.TeleBot(token)
user_calc = False
user_calc_comp = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>!\nДобро пожаловать в калькулятор.'
                                      f'\nВоспользуйся меню для продолжения.', parse_mode='html')
    log.logger_start()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    calc = types.KeyboardButton('Рациональные числа')
    calc_comprehensive = types.KeyboardButton('Комплексные числа')
    user_log = types.KeyboardButton('История операций')
    markup.add(calc, calc_comprehensive, user_log)
    bot.send_message(message.chat.id, 'Меню:', reply_markup=markup)

@bot.message_handler(content_types='text')
def text_message(message):
    global user_calc
    global user_calc_comp
    if message.text == 'Рациональные числа':
        log.logger_button(message.text)
        bot.send_message(message.chat.id, 'Введите пример:')
        user_calc = True
    elif message.text == 'Комплексные числа':
        log.logger_button(message.text)
        bot.send_message(message.chat.id, 'Введите пример комплексных чисел:')
        user_calc_comp = True
    elif message.text == 'История операций':
        log.logger_button(message.text)
        logs = open('logs.txt', 'rb')
        bot.send_document(message.chat.id, logs)
    elif user_calc:
        bot.send_message(message.chat.id, buttons.button_calc(message.text))
        user_calc = False
    elif user_calc_comp:
        bot.send_message(message.chat.id, buttons.button_calc_comp(message.text))
        user_calc_comp = False
    else:
        bot.send_message(message.chat.id, 'Я Вас не понял(')


bot.polling(none_stop=True)

