# import time
#
# start_time = time.time()
# l = [i for i in range(3000000)]
# print("ДА" if 2999999 in set(l) else "НЕТ")
# stop_time = time.time()
# print(f"{stop_time- start_time} seconds")  # 0.4882779121398926 seconds
#
# start_time2 = time.time()     1 ужасно неудовлетворительно удовлетворительно прилично отлично
# l2 = [i for i in range(3000000)]
# print("ДА" if 2999999 in l2 else "НЕТ")
# stop_time2 = time.time()
# print(f"{stop_time2 - start_time2} seconds")  # 0.252194881439209 seconds

# text = [i.lower() for i in input().split()]
# res = {i: text.count(i) for i in set(text)}
# print(res.get('и') if 'и' in res.keys() else 0)

lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине',
        'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
lst_in = [i.split(':') for i in lst_in]
# print(lst_in)
d = {i[0]: set() for i in lst_in}
for i in d:
    for j in lst_in:
        if i in j:
            d[i].add(j[1])
print(d)
# res =
