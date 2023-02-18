#
# a1 = int(input())
# d = int(input())
# n = int(input())
#
# for i in range(n):
#     print(a1 + i * d)

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minimum = int(input())
maximum = int(input())
print([ind for ind, num in enumerate(arr) if minimum <= num <= maximum])
