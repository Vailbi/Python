import random
# d = {'cat': 'кот', 'horse':'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book':'книга'}
#
#
# def get_sort(x):
#     temp = sorted(x, reverse=True)
#     res = [x[i] for i in temp]
#     return res
#
#
# print(get_sort(d))
#
#
# def get_sort2(dic):
#     return list(map(lambda x: dic[x], sorted(dic, reverse=True)))
#
# print(get_sort2(d))

# lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
# arr = dict(list(map(lambda x: (x[0], int(x[1])), [i.split(':') for i in lst_in])))
# print(*sorted(arr, key=lambda x:arr[x])[:3])


# lst_in = [
#     'Номер;Имя;Оценка;Зачет',
#     '1;Портос;5;Да',
#     '2;Арамис;3;Да',
#     '3;Атос;4;Да',
#     '4;д\'Артаньян;2;Нет',
#     '5;Балакирев;1;Нет'
# ]
# arr = [i.split(';') for i in lst_in]  # lst 1-0 temp, lst 3-1 temp, lst 2-2 temp, lst 0-3 temp
# # arr = list(map(lambda x: (x[3],x[1],int(x[2]),int(x[0])),arr[1:]))
# temp = [1, 3, 2, 0]
# temp_dic = {'Имя': 1, 'Зачет': 3, 'Оценка': 2, 'Номер': 0}
#
# result = (('Имя', 'Зачет', 'Оценка', 'Номер'),
#           ('Портос', 'Да', 5, 1),
#           ('Арамис', 'Да', 3, 2),
#           ('Атос', 'Да', 4, 3),
#           ("д'Артаньян", 'Нет', 2, 4),
#           ('Балакирев', 'Нет', 1, 5)
#           )
#
# n=[0,2,1] # 0 это 0 индекс, 2 это 1 индекс, 1 это 2 индекс
# a=("a","b","c")
# print(sorted(a, key=lambda x: n.index(a.index(x))))
# res = [tuple(sorted(i, key=lambda x: temp.index(i.index(x)))) for i in arr]
# print(res[0],*map(lambda x: (x[0],x[1],int(x[2]),int(x[3])), res[1:]))
#
# t_sorted = tuple([
#     (name, passed, int(mark) if mark.isdigit() else mark, int(num) if num.isdigit() else num)
#     for num, name, mark, passed in [el.split(';') for el in lst_in]
# ])
#
# print(t_sorted)

lst_in = ['рядовой', ' сержант', ' старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
temp = dict(list(zip(lst_in,range(len(lst_in)))))
test = ['рядовой', ' полковник', ' сержант', ' старшина', ' прапорщик', ' подполковник', ' капитан', ' лейтенант', ' майор']
print(temp)
lst = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан",
          'Арамис=лейтенант', 'Балакирев=рядовой']
print(list(i.split('=') for i in sorted(lst, key=lambda x: temp[x.split('=')[1]])))

# order = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'
# lst = [x.split('=') for x in lst_in]
# lst = sorted(lst, key=lambda x: order.find(x[1]))
