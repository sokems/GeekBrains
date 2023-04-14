# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

import time
import json

def add_note(title, text):
    try:
        with open("notes.json", "r", encoding='utf-8') as file:
            notes = json.load(file)

        if len(notes) == 0:
            id_note = 0
        else:
            id_note = len(notes)

        create_time = time.strftime("%H:%M | %d.%m.%Y", time.localtime())
        new_note = {'id': id_note, 'create': create_time, 'title': title, 'text': text, 'edit': None}
        notes.append(new_note)

        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file)
        print(f'Заметка с ID {id_note} создана!')

    except:
        print(f'Заметка не создана. Попробуйте снова!')

def read_notes():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    if len(notes) == 0:
        print('Список заметок пуст!')
    else:
        for note in notes:
            if note["edit"] is None:
                print(f'ID заметки: {note["id"]}\nДата создания: {note["create"]}\n{note["title"]}')
            else:
                print(f'ID заметки: {note["id"]}\nДата создания: {note["create"]}\n{note["title"]}')
            print('-' * 20)

def check_note(id_note):
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    if len(notes) == 0:
        return False
    else:
        for note in notes:
            if id_note.isdigit() and note["id"] == int(id_note):
                return True
        return False

def read_one_note(id_note):
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    if check_note(id_note):
        for note in notes:
            if id_note.isdigit():
                if note["id"] == int(id_note):
                    if note["edit"] is None:
                        print(f'ID заметки: {note["id"]}\nДата создания: {note["create"]}\n\n{note["title"]}\n'
                              f'{note["text"]}\n\nПоследняя дата изменения: Не изменялась')
                    else:
                        print(f'ID заметки: {note["id"]}\nДата создания: {note["create"]}\n\n{note["title"]}\n'
                              f'{note["text"]}\n\nПоследняя дата изменения: {note["edit"]}')
                    print('-' * 20)
    else:
        print('Заметки не существует')

def delete_note(id_note):
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    if check_note(id_note):
        for i in range(len(notes)):
            if id_note.isdigit():
                if notes[i]["id"] == int(id_note):
                    del notes[i]
                    break
        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file)
        print(f'Заметка с ID {id_note} удалена!')
    else:
        print('Заметки не существует')

def edit_note(id_note, param, message):
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    for note in notes:
        if id_note.isdigit():
            if note["id"] == int(id_note):
                if param == 1:
                    note["title"] = message
                    edit_time = time.strftime("%H:%M | %d.%m.%Y", time.localtime())
                    note["edit"] = edit_time
                elif param == 2:
                    note["text"] = message
                    note["edit"] = edit_time
                else:
                    print('Неверно указан параметр!')

    with open("notes.json", "w", encoding='utf-8') as file:
        json.dump(notes, file)
    print(f'Заметка с ID {id_note} отредактирована!')

def main():
    while True:
        print('-' * 100)
        print('Список команд:\n1. Добавить заметку\n2. Вывести список заметок\n3. Прочитать заметку\n'
              '4. Редактировать заметку\n5. Удалить заметку\n')
        command = input('Введите цифру команды: ')
        if int(command) == 1:
            title = input('Введите заголовок заметки: ')
            text = input('Введите текст заметки: ')
            add_note(title, text)
        elif int(command) == 2:
            read_notes()
        elif int(command) == 3:
            id_note = input('Введите ID заметки: ')
            read_one_note(id_note)
        elif int(command) == 4:
            id_note = input('Введите ID заметки: ')
            if check_note(id_note):
                print('Список параметров для редактирования:\n1. Заголовок\n2. Текст\n')
                param = input('Введите цифру параметра: ')
                message = input('Введите новое значение: ')
                edit_note(id_note, param, message)
            else:
                print('Заметки не существует')
        elif int(command) == 5:
            id_note = input('Введите ID заметки: ')
            delete_note(id_note)
        else:
            print('Некорректная команда!')

main()