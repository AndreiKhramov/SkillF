def field_print(func):
    for i in range(1, 10):
        if i % 3 == 0:
            print(func[i - 3:i])


def menu():
    print(' -------------------------------------------------------------------------------- ')
    print('Поле для игры имеет следующий вид')
    field_rules = [i for i in range(0, 9)]
    for i in range(1, 10):
        if i % 3 == 0:
            print(field_rules[i - 3:i])
    print('Для осуществления хода необходимо нажать соответствующую цифру, начинают "X"')
    print(' -------------------------------------------------------------------------------- ')
    return True


def win_condition():
    # функция для сравнения выигрышных срезов
    def compare(cond):
        return cond == ([field[j]] * 3) != (['| |'] * 3)

    while True:
        # срез по вертикали
        for j in range(0, 9, 3):
            if compare(field[j:j + 3]):
                print(f'Выиграли {field[j]}')
                return True
            break

        # срез по горизонтали
        for j in range(0, 9):
            if compare(field[j:j + 9:3]):
                print(f'Выиграли {field[j]}')
                return True
            # диагонали
            if compare([field[0], field[4], field[8]]) or compare([field[2], field[4], field[6]]):
                print(f'Выиграли {field[j]}')
                return True
            break

        return False


field = ['| |' for i in range(9)]
counter = 0
menu()

while True:
    button = input()

    if button.isdigit():
        button = int(button)
        if button not in range(9):
            print('Выбрана неверная цифра')
            continue
    else:
        print('Введен неверный символ - введите цифру от 0 до 8')
        continue

    if field[button] != '| |':
        print('Данная позиция занята, выберите другую клетку')
        continue

    if counter % 2 == 0:
        field[button] = '|X|'
    else:
        field[button] = '|0|'

    counter += 1
    if counter % 2 == 0:
        print('Ходит "X"')
    else:
        print('Ходит "0"')
    field_print(field)
    # раньше 5 хода не проверяется выигрыш
    if counter >= 5:
        if win_condition():
            break
    if counter == 9:
        print('Ничья')
        break

    continue
