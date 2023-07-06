# # пример
# a = [1 for x in range(5)]
# print(a)  # [1, 1, 1, 1, 1]
#
# a = [0.5 * x + 1 for x in range(7)]
# print(a)  # [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
#
# a = [x for x in range(-5, 5) if x % 2 == 0]
# print(a)  # [-4, -2, 0, 2, 4]
#
# d = [4, 3, 5, 0, 2, 11, 122, -8, 9]
# a = ['четное' if x%2 == 0 else 'нечетное'
#      for x in d]
# print(a)  # ['четное', 'нечетное', 'нечетное', 'четное', 'четное', 'нечетное', 'четное', 'четное', 'нечетное']


# num = int(input())
# arr = [print(*[1 if x == i else 0 for x in range(num)]) for i in range(num)]
# # 1 0 0 0
# # 0 1 0 0
# # 0 0 1 0
# # 0 0 0 1

# num = int(input())
# print(*[x for x in range(1,num+1) if num%x == 0])  # делители числа num

# num = int(input())
# arr = [print(*[i for x in range(num)]) for i in range(num)]
# for i in arr:
#     print(*i)

# результат

# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

# n = int(input())
# [print(*[i]*n) for i in range(n)]


# сложение элементов двух списков
# крутой вариант запомнить!!!!!!!!!!!!!!!!!!!!!!!!!!!


# num = list(map(int, input().split()))
# num1 = list(map(int, input().split()))
# res = [(num[i] + num1[i]) for i in range(len(num))]
# print(*res)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Sample Input:
# Москва 15000 Уфа 1200 Самара 1090 Казань 1300
# Sample Output:
# [['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]

# city = input().split()
#
# res = [[city[i], int(city[i+1])] for i in range(0,len(city)-1,2)]
# print(res)

# import antigravity   хахахахахахаха
# print(...)

# Снова примеры!
# !!!!!!!!!!!
# !!!!!!!!!!!!
# !!!!!

table = []