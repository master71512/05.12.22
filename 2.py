# 2) Создайте программу для игры в ""Крестики-нолики"".

print('Игра крестики-нолики\n\
Игровое поле состоит из 9 квадратов с номерами от 1 до 9:\n\
1\t2\t3\t\n4\t5\t6\t\n7\t8\t9\n\
Чтобы сделать ход, игрок вводит номер свободного квадрата,\n\
в котором хочет поставить свой знак.\n\
Для 1-го игрока автоматически ставится х, для второго - 0\n\
Первый ход делает игрок 1.')

field = [[i for i in range(1, 4)], [i for i in range(4, 7)], [
    i for i in range(7, 10)]]

def PrintField(f):
    for i in f:
        print('\t'.join(list(map(str, i))))

def IsWinner(array):
    flag = False
    for i in range(len(array)):
        if array[i][0] == array[i][1] == array[i][2]:
            flag = True
        if array[0][i] == array[1][i] == array[2][i]:
            flag = True
    if array[0][0] == array[1][1] == array[2][2]:
        flag = True
    if array[0][2] == array[1][1] == array[2][0]:
        flag = True
    return flag

def Step(player, array, counter):
    num = int(
        input(f'{player}, введите номер свободного места на игровом поле от 1 до 9\n'))
    while num < 1 or num > 9:
        num = int(input('Можно ввести только число от 1 до 9! Повторите ввод\n'))
    flag = False
    while not flag:
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == num:
                    flag = True
                    if counter % 2 == 1:
                        array[i][j] = 'X'
                    else:
                        array[i][j] = 0
        if not flag:
            num = int(
                input(f'{player},введите другой номер, это место занято!\n'))

player1 = input("Кто будет ходить первым и ставить Х?\n")
player2 = input("Кто будет ходить вторым и ставить 0?\n")
counter = 0
while not IsWinner(field):
    player = player1
    counter += 1
    Step(player, field, counter)
    PrintField(field)
    if counter > 4:
        if IsWinner(field):
            print(f'{player} победил')
    if not IsWinner(field):
        player = player2
        counter += 1
        Step(player, field, counter)
        PrintField(field)
        if IsWinner(field):
            print(f'{player} победил')
