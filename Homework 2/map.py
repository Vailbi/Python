lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']
 # здесь передается аргумент в мэп через генератор. т.е. берется и
# print(res)  # [[8, 11, -5], [3, 4, 10], [-1, -2, 3], [-4, 5, 6]]
test = 'house=дом car=машина men=человек tree=дерево'
print(test.split())
res = list(list(map(int, i.split())) for i in lst_in)
res2 = tuple(tuple(map(tuple, i.split('=')) for i in test.split()))
tes2 = tuple(tuple(i.split('=')) for i in test.split())

print(res2)
print(tes2)
