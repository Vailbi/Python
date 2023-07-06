# # +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# lst = sorted(input().split())
# d = {}
# for i in lst:
#     kod = i[:2]
#     if kod in d:
#         d[i[:2]].append(i)
#     else:
#         d[i[:2]] = []
#         d[i[:2]].append(i)
# print(d)
# print(*sorted(d.items()))
# lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# lst_in = [i.split() for i in lst_in]
# d = {}
# это мое решение!
# for i in lst_in:
#     day = i[0]
#     if day in d:
#         d[day].append(i[1])
#     else:
#         d[day] = []
#         d[day].append(i[1])
#
# for key,value in d.items():
#     print(f'{key}:', ', '.join(value))


# d = {}
#
# for i in lst_in:
#     key, value = i.split()
#     print(key, value)
#     d[key] = d.get(key, []) + [value]
# print(d)
# максимальное значение 12560
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
N = int(input()) * 1000
array_value = sorted(things.values(), reverse=True)
result = []
for i in array_value:
    if N - i >= 0:
        N = N-i
        result.append(i)
for i in result:
    for key, value in things.items():
        if value == i:
            print(key, end= ' ')


