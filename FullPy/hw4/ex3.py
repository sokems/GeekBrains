"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""


def replenish(action, count_plus):
    if action % 50 == 0:
        if count_plus % 3 == 0:
            action -= action * 0.03
        if action >= 5_000_000:
            action -= action * 0.1

        return action

    else:
        return -1


def withdrawal(action, count_minus, balance):
    if action % 50 == 0:
        if action * 0.015 < 30:
            if count_minus % 3 == 0:
                if balance >= action + 30 + (action * 0.03):
                    balance -= action + 30 + (action * 0.03)

            else:
                if balance >= action + 30:
                    balance -= action + 30

        elif action * 0.015 > 600:
            if action >= 5_000_000:
                if count_minus % 3 == 0:
                    if balance >= action + 600 + (action * 0.03) + (action * 0.1):
                        balance -= action + 600 + (action * 0.03) + (action * 0.1)

                else:
                    if balance >= action + 30 + (action * 0.1):
                        balance -= action + 30 + (action * 0.1)

            else:
                if count_minus % 3 == 0:
                    if balance >= action + 600 + (action * 0.03):
                        balance -= action + 600 + (action * 0.03)

                else:
                    if balance >= action + 30:
                        balance -= action + 30

        else:
            if count_minus % 3 == 0:
                if balance >= action + (action * 0.015) + (action * 0.03):
                    balance -= action + (action * 0.015) + (action * 0.03)

            else:
                if balance >= action + (action * 0.015):
                    balance -= action + (action * 0.015)
        return balance

    else:
        return -1


use = 0
balance = 0
count_plus = 0
count_minus = 0
history_oper = []

while True:
    action = input('\nВыберите действие:\n1. Пополнить\n2. Снять\n3. Выйти\n')

    if action == '1':
        count_plus += 1
        action = replenish(float(input('Введите сумму пополнения (кратно 50 у.е.): ')), count_plus)
        if action == -1:
            print('Сумма должна быть кратна 50 у.е.!')
        else:
            balance += action
            history_oper.append(('Пополнение', action))

        print(f'Ваш баланс: {balance} у.е.')

    elif action == '2':
        count_minus += 1
        print(f'Ваш баланс: {balance} у.е.')
        action = withdrawal(float(input('Введите сумму снятия (кратно 50 у.е.): ')), count_minus, balance)
        if action == -1:
            print('Сумма должна быть кратна 50 у.е.!')
        else:
            history_oper.append(('Снятие', balance - action))
            balance = action

        print(f'Ваш баланс: {balance} у.е.')

    elif action == '3':
        break
