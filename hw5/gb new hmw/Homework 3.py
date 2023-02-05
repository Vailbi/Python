# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Задача 20

# word = input()
# result = 0
# for i in word:
#     if i.lower() in 'aeioulnstrавеинорст':
#     elif i.lower() in 'dgдклмпу':
#         result += 2
#     elif i.lower() in 'bcmpбгёья':
#         result += 3
#     elif i.lower() in 'fhvwyйы':
#         result += 4
#     elif i.lower() in 'kжзхцч':
#         result += 5
#     elif i.lower() in 'jxшэю':
#         result += 8
#     elif i.lower() in 'qzфщъ':
#         result += 10
# print(result)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# search = list(i for i in range(1, int(input())))
# num = int(input())
# print(*search)
# print(search.count(num))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai

size = int(input())
search = list(i for i in range(size))
num = int(input())
result = 0
if num > len(search):
    result = search[-1]
elif num >= 0 and num <= size:
    result = f'{num-1} или {num+1}'
elif num < 0:
    result = 0
print(*search)
print(result)