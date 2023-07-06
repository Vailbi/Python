# n = 3
# arr = list(range(1,sum(range(n+1))*2,2))
#
# print(arr)
#

# n = 19
# x = n*(n-1)+1
# print(x)
# res = sum(range(x,sum(range(n+1))*2,2))
# print (res)
#
# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#
# stroka1 = input()
# stroka2 = input()
#
# print(stroka2.count(stroka1))
import sympy
# from sympy import Symbol
# x = Symbol('x')
# y = Symbol('y')
# expr = x**2 + y**2
# print(expr)

# # put your python code here
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# arr = map(int,input().split())
# result = [m[i-1] for i in arr]
# for i in range(len(result)):
#     if result[i] == 'до' or result[i] == 'фа':
#         result[i] = '#'+result[i]
#
# print(*result)
#
#



# put your python code here
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



# text = list(input('Введите текст:').split())
# for i, j in enumerate(text):
#     if 'абв' in j:
#         del text[i]
# print(*text)
#



# import sympy
# result = input('Введите уравнение: ') # например (1+2)*3
# print(sympy.simplify(result))

def AI_step (number):
    print(' * Ходит  компьютер')
    print('---------')
    player_2 = number % 29 if number % 29!=0 else random.randint(1, 29)

    print(f'Компьтер взял {player_2} конфет ')
    return player_2

import random
print("Игра с конфетами")
print(' * На столе лежит 121 конфета. Играют два игрока делая ход друг после друга. \n'
      ' * Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \n'
      ' * Все конфеты оппонента достаются сделавшему последний ход. \n')
total = 121
begin = random.randint(0, 1)

def AI_player(score, priority):

    while score > 0:

        if priority == 0:
            player = 1
            print(' * Ходит первый игрок')
            player_1 = int(input('Количество взятых конфет: '))
            while player_1 <= 0 or player_1 > 28:
                player_1 = int(input('Неверное количество конфет! Введите число от 1 до 28: '))
            score -= player_1
            if player == 1:
                priority = 1
            print(f' * Осталось {score} конфет')
        else:
            player = 2

            # print(' * Ходит второй игрок')
            player_2 = AI_step(score)
            # while player_2 <= 0 or player_2 > 28:
            #     player_2 = int(input('Неверное количество конфет! Введите число от 1 до 28: '))
            score -= player_2
            if player == 2:
                priority = 0
            print(f' * Осталось {score} конфет')

    else:
        if player == 1:
            return ' * * * Победил первый игрок * * * '
        else:
            player == 2
            return ' * * * Победил компютер * * * '


def Two_player(score, priority):

    while score > 0:

        if priority == 0:
            player = 1
            print(' * Ходит первый игрок')
            player_1 = int(input('Количество взятых конфет: '))
            while player_1 <= 0 or player_1 > 28:
                player_1 = int(input('Неверное количество конфет! Введите число от 1 до 28: '))
            score -= player_1
            if player == 1:
                priority = 1
            print(f' * Осталось {score} конфет')
        else:
            player = 2

            print(' * Ходит второй игрок')
            player_2 = int(input('Количество взятых конфет: '))
            while player_2 <= 0 or player_2 > 28:
                 player_2 = int(input('Неверное количество конфет! Введите число от 1 до 28: '))
            score -= player_2
            if player == 2:
                priority = 0
            print(f' * Осталось {score} конфет')

    else:
        if player == 1:
            return ' * * * Победил первый игрок * * * '
        else:
            player == 2
            return ' * * * Победил второй игрок * * * '

print(AI_player(121, begin)) # вывод с ИИ

# print(Two_player(121,begin)) # игра на двоих