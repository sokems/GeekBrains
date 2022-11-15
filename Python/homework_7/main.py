import buttons
import easygui
import log

log.logger_start()

def start_gui():
    while True:
        button = easygui.buttonbox('Выберите действие: ', 'Homework_7', ['Калькулятор', 'История операций', 'Выход'])

        if button == 'Калькулятор':
            buttons.button_calc()

        if button == 'История операций':
            buttons.button_log()

        if button == 'Выход':
            log.logger_exit()
            quit()


start_gui()