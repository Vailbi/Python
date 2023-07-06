# from string import ascii_lowercase, ascii_uppercase
# import random
# random.seed(1)
# chars = ascii_lowercase + ascii_uppercase
#
# # генератор email
# def gengen(n):
#     for i in range(n):
#         yield "".join([chars[random.randint(0, len(chars))-1] for i in range(n)])+f"@mail.ru"
#
# N = int(input())
# x = gengen(N)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# def gen(n):
#     default = [1, 1, 1]
#     for i in range(2,n-1):
#         res = sum(default[len(default)-3:])
#         default.append(res)
#     for j in default:
#         yield j
#
#
# n = int(input())
# aa = gen(n)
# print(*list(aa))
#
# #1, 1, 1, 3, 5, 9, 17, 31, 57, ... последовательность сумма поседних 3 чисел
# N = int(input())
#
#
# def get_sum(N):
#     a = b = c = 1
#     for _ in range(N):
#         yield a
#         a, b, c = b, c, a + b + c

N = int(input())
k = 0
arr = []
for i in range(2,N+1):
    for j in range(2,i):
        if i%j ==0:
            k+=1
    if k==0:
        arr.append(i)
    else:
        k=0
print(*arr)