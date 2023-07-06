# # Задача 34
#
#
# def res(txt):
#     txt = txt.split()
#     return [i.count('а') for i in txt]
#
#
# def rifma(arr):
#     print('Парам пам-пам' if max(arr) == min(arr) else 'Пам парам')
#
#
# rifma(res(input()))


# Задача 36


num_rows = int(input())
num_columns = int(input())


def f_print(fun, x, y):
    [print(*[str(fun(x, y)) for x in range(1, x + 1)]) for y in range(1, y + 1)]


f_print(lambda x, y: x * y, num_rows, num_columns)
