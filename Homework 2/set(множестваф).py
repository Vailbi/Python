b = {1,3,46,7,'pupa'}
a = set() # определить множество  a = {}
a.add(1) # добавить значение к множеству
a.update(b) # добавить несколько элементов, итерированный объект
c = set('абракадабра') # {'б', 'д', 'а', 'р', 'к'}
c.discard('д') # удалить элемент, если элемента нет в множестве то ошибка не выдается remove() тоже удаляет, но может вернуть ошибку


# text = set(i for i in input() if i in "0123456789")
# if len(text)>0:
#     print(*sorted(set(i for i in input() if i in "0123456789")))
# else:
#     print('НЕТ')

res = set()
text = input()
while text != 'q':
    res.add(text)
    text = input()
print(len(res))
# print(len(set(i for i in iter(input, 'q'))))
# set(i for i in iter(input, 'q')) # генератор множества iter будет считывать пока не попадется 'q'
# len() # длина множества т.к. множество состоит только из уникальных элементов