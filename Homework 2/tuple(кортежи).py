# a = 2, # <class 'tuple'>     (2,)
# print(a)
# x, y = ['привет', 'Мурик'] #  x = привет y = Мурик
#
# primer = (['pupa'], 'lupa')
# primer[0].append(['zalupa']) #(['pupa', ['zalupa']], 'lupa')
# print(primer)
#
#
# t = input().split()
# if 'Москва' in t:
#     t.
#     t=tuple(t)
# else:
#     x = t.index("Ульяновск")
#     t.append('Москва')
#     t = tuple(t)
# print(*list(t))

# пример с сайта
# это нахывется печать в слепу.
# t = tuple(input().split())
# t = t + ('Москва',) if 'Москва' not in t else t
# print(*t)

# Подвиг 5. Вводятся названия городов в одну строку через пробел.
# На их основе формируется кортеж. Если в этом кортеже присутствует город "Ульяновск", то этот элемент следует удалить (создав новый кортеж).
# Результат вывести на экран в виде строки с названиями городов через пробел.

# t = tuple([x.lower() for x in input().split()])
# t = tuple(v.lower() for v in [x.lower() for x in input().split()] if 'ва' in v)
# print(*tuple(v.lower() for v in [x.lower() for x in input().split()] if 'ва' in v))


# arr = tuple(map(int, input().split()))
# res = tuple([ind for ind,num in enumerate(arr) if arr.count(num)>1])
# print(*res)


# Вводится натуральное число N (N < 5).
# Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов.
# Результат вывести на экран в виде таблицы чисел.

num = int(input())

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
t2 = tuple([tuple([t[i][j] for j in range(num)]) for i in range(num)])
for i in t2:
    print(*i)


