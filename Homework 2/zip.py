# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# res = map(lambda x: x[0]*x[1],zip(a,b))
# for i in range(3):
#     print(next(res), end=' ')
#
# # version on Stepik  пример передачи в мэп двух итеррируемых объектов
# lst1 = map(int, input().split())
# lst2 = map(int, input().split())
#
# lst = map(lambda x, y: x * y, lst1, lst2)
#
# print(*(next(lst) for _ in range(3)))

# lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
# arr = map(str.split, lst_in)  # tuple(i.split()for i in lst_in) чтобы использовать сплит поставлена стр.сплит
# print(*arr)
# res = zip(*zip(*arr))
# for i in res:
#     print(*i)


# city = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
# city = city.split()
# it_city = iter(city)
# arr_city = []
# for i in range(3):
#     arr_city.append(tuple(next(it_city) for j in range(3)))
# res = zip(*arr_city)
# for _ in res:
#     print(*_)
#
# x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])
# print(*zip(x, x, x, x))  # (1, 2, 3) (4, 5, 6) (7, 8, 9)

# s = 'Pytnon дай мне сил пройти этот курс до конца!'
# res = iter(s.split())
# num = [i for i in range(len(s))]
# lst1 = [*zip(s,num)]
# lst = lst1[:10]
# print(lst)

