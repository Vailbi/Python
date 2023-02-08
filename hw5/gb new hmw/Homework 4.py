# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# size1 = int(input('Введите n кол-во 1-го множества: '))
# size2 = int(input('Введите ь кол-во 2-го множества: '))
# arr1 = list(i for i in range(size1))
# arr2 = list(i for i in range(size2))
# print('Введите элементы первого множества:')
# for i in range(len(arr1)):
#     arr1[i] = int(input())
# print(arr1)
# print('Введите элементы второго множества:')
# for i in range(len(arr2)):
#     arr2[i] = int(input())
# print(arr1)
# result = []
# for i in arr1:
#     if i in arr2:
#         result.append(i)
#
# print()
# print(*sorted(set(result)))
#

# Задача 24

kust = int(input())-1
result = 0
if kust == 0:
    result = kust + kust + 1
    print(result)
else:
    result = kust + (kust-1) + (kust+1)
    print(result)