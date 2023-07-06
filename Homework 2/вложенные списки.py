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
#

# lst_in = [[1, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
# result = ''
# for i in range(4):
#     for j in range(4):
#         summa = lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1]
#         if summa <= 1:
#             result='ДА'
#         else:
#             result = 'НЕТ'
#             print(result)
#             exit()
# print(result)

# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]
# res = ''
# for i in range(len(lst_in)):
#     for j in range(i+1,len(lst_in)):
#         if lst_in[i][j] == lst_in[j][i]:
#             res = 'ДА'
#         else:
#             res = 'НЕТ'
#             print(res)
#             exit()
# print(res)

# arr = [1, 5, 1, 5, 1,2,3,2,4,5,6,10,6]
# result = 0
# for i in range(1,len(arr)-1):
#     if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
#         result+=1
# print(result)

# arr = list(map(int, input().split()))
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j+1]<arr[j]:
#             temp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = temp
# print(arr)


# Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
# Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n?
# Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей).
# Предполагается, что имеется достаточно большое количество купюр всех достоинств.

# num = int(input())
# res = []
# for i in range(6,-1,-1):
#     if num//(2**i) > 0:
#         temp = num//(2**i)
#         num = num - ((2**i)*temp)
#         for j in range(temp):
#             res.append(2**i)
# print(*res)

n = int(input())
s = ''
for i in (64, 32, 16, 8, 4, 2, 1):
    k = n // i
    s += f'{i} ' * k
    n -= i * k

print(s)