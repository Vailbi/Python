# text = input() # Барабанщик бил бой в барабан
# result = []
# for index, word in enumerate(text):
#     if word == 'р' and text[index+1] == 'а':
#         result.append(index)
# if len(result) == 0:
#     print(-1)
# else:
#     print(*result)
#
# # s = input().lower()
# # count = 0
# #
# # for i in range(len(s) - 1):
# #     if s[i] + s[i + 1] == 'ра':
# #         count += 1
# #         print(i, end=' ')
# # if count == 0:
# #     print(-1)

# number = input()
# new_number = list(filter(lambda x: x.isdigit(), list(number[:])))
# if number[0] == '+' and number[2] == '(' and number[6] == ')' and number[10] == '-' and number[13] == '-' and len(number)==16\
#         and len(new_number) == 11:
#     print('ДА')
# else:
#     print('НЕТ')

# "10 + 25 - 12 + 20 - 1 + 3"


# Необходимо выполнить вычисление и результат отобразить на экране.
# Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-),
# а в качестве операндов - целые неотрицательные числа.
# Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
# n = input()
# n = n.replace(' ', '')
# n = n.replace('+', '_+')
# n = n.replace('-', '_-')
# k = list(map(int, n.split('_')))
# print(sum(k))
# n = input()
# print(eval(n))

# arr = list(map(int, input().split()))
# resultarr = list(y**2 for x,y in enumerate(arr))
#
# print(*resultarr)

# arr = list(map(int, input().split()))
# new_arr = []
# for indx,value in enumerate(arr):
#     for x in range(2):
#         new_arr.append(value)
# print(*new_arr)

# arr = list(map(float, input().split()))
# res_arr = []
# for indx,value in enumerate(arr):
#     if value > 0:
#         res_arr.append(value)
#     else:
#         res_arr.append(-1.0)
# print(*res_arr)


# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# a = int(input())
# b = int(input())
# def Stepen(x,y):
#     while y != 1:
#         return Stepen(x,y-1)*x
#     return x
# print(Stepen(a,b))
#

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# a = int(input())
# b = int(input())
# def Summa(x,y):
#     while y != 0:
#         return Summa(x+1,y-1)
#     return x
# print(Summa(a,b))

# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
# c = []
#
# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#     c.append(r)
#
# print(c)


#
# Подвиг 1. Вводится натуральное число N (то есть, положительное, целое). Требуется создать двумерный (вложенный) список размером N x N элементов,
# состоящий из всех единиц, а затем, в последний столбец записать пятерки. Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
#
# P.S. Будьте внимательны в конце строк пробелов быть не должно!
# num = int(input())
# matrix = []
# for i in range(num):
#     matrix.append([0]*num)
# for ind, value in enumerate(matrix):
#     for j in range(len(value)):
#         if j != len(value)-1:
#             value[j] = 1
#         else:
#             value[j] = 5
# for i in matrix:
#     print(*i)
#
#
# n = int(input())   # короткая версия кода
# lst = [[1] * n] * n
# lst[0][n-1] = 5
#
# for i in lst:
#     print(*i)

text = input()


def Zip(txt):

    result = ''
    count = 1
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count+=1
        else:
            result+=txt[i]+str(count)
            count=1
        if i == len(txt)-2:
            result += txt[len(txt)-1]+str(count)

    return result


def Reversed(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False


print(Zip(text))
print(Reversed(text))



