"""✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

use = 0
balance = 0
count_plus = 0
count_minus = 0

while True:
    if use == 0:
        action = input('\nВыберите действие:\n1. Пополнить\n2. Снять\n3. Выйти\n')

        if action == '1':
            use = 1
            count_plus += 1
            action = float(input('Введите сумму пополнения (кратно 50 у.е.): '))

        elif action == '2':
            use = 2
            count_minus += 1
            print(f'Ваш баланс: {balance} у.е.')
            action = float(input('Введите сумму снятия (кратно 50 у.е.): '))

        elif action == '3':
            break

    elif use == 1:
        if action % 50 == 0:
            use = 0
            balance += action
            if count_plus % 3 == 0:
                balance -= action * 0.03
            if action >= 5_000_000:
                balance -= action * 0.1

            print(f'Ваш баланс: {balance} у.е.')

        else:
            action = float(input('Введите сумму пополнения (кратно 50 у.е.): '))

    elif use == 2:
        use = 0
        if action % 50 == 0:
            if action * 0.015 < 30:
                if count_minus % 3 == 0:
                    if balance >= action + 30 + (action * 0.03):
                        balance -= action + 30 + (action * 0.03)
                        print(f'Ваш баланс: {balance} у.е.')

                    else:
                        print(f'Ваш баланс: {balance} у.е.')

                else:
                    if balance >= action + 30:
                        balance -= action + 30
                        print(f'Ваш баланс: {balance} у.е.')

                    else:
                        print(f'Ваш баланс: {balance} у.е.')

            elif action * 0.015 > 600:
                if action >= 5_000_000:
                    if count_minus % 3 == 0:
                        if balance >= action + 600 + (action * 0.03) + (action * 0.1):
                            balance -= action + 600 + (action * 0.03) + (action * 0.1)
                            print(f'Ваш баланс: {balance} у.е.')

                        else:
                            print(f'Ваш баланс: {balance} у.е.')

                    else:
                        if balance >= action + 30 + (action * 0.1):
                            balance -= action + 30 + (action * 0.1)
                            print(f'Ваш баланс: {balance} у.е.')

                        else:
                            print(f'Ваш баланс: {balance} у.е.')

                else:
                    if count_minus % 3 == 0:
                        if balance >= action + 600 + (action * 0.03):
                            balance -= action + 600 + (action * 0.03)
                            print(f'Ваш баланс: {balance} у.е.')

                        else:
                            print(f'Ваш баланс: {balance} у.е.')

                    else:
                        if balance >= action + 30:
                            balance -= action + 30
                            print(f'Ваш баланс: {balance} у.е.')

                        else:
                            print(f'Ваш баланс: {balance} у.е.')

            else:
                if count_minus % 3 == 0:
                    if balance >= action + (action * 0.015) + (action * 0.03):
                        balance -= action + (action * 0.015) + (action * 0.03)
                        print(f'Ваш баланс: {balance} у.е.')

                    else:
                        print(f'Ваш баланс: {balance} у.е.')

                else:
                    if balance >= action + (action * 0.015):
                        balance -= action + (action * 0.015)
                        print(f'Ваш баланс: {balance} у.е.')

                    else:
                        print(f'Ваш баланс: {balance} у.е.')

        else:
            use = 2
            action = float(input('Введите сумму снятия (кратно 50 у.е.): '))
