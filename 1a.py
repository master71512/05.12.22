# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

from random import randint
N = 120
max_choice = 28
print('На столе лежит 120 конфет.\nИграют два игрока, делая ход друг после друга.\n\
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.\n\
Победитель - тот, кто оставил на столе 0 конфет.')
player = input('Введите имя игрока:\n')
while N > 0:
    if N > 0:
        now_play = player
        print('Конфет:', N)
        print(
            f'Сейчас ходит {now_play}, сколько возьмете конфет? (от 1 до 28 включительно)')
        player_choice = int(input())
        while player_choice > N:
            print(
                f"Осталось всего {N} конфет, нельзя взять больше! Так сколько берете?")
            player_choice = int(input())
        while player_choice > 28 or player_choice < 1:
            print('Можно взять только от 1 до 28 конфет, так сколько берете?')
            player_choice = int(input())
        N -= player_choice
    if N > 0:
        now_play = 'бот'
        print('Конфет:', N)
        print(
            f'Сейчас ходит {now_play}, сколько возьмете конфет? (от 1 до 28 включительно)')
        if N > max_choice:
            bot_choice = randint(1, max_choice)
        else:
            bot_choice = N
        print(bot_choice)
        N -= bot_choice
print('Победитель -', now_play)
