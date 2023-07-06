# Оставляй комментарии!!!
lst = input().split()
d = {}
for i in lst:
    kod = i[:2]
    if kod in d.keys():
        d[kod] += [i]
        continue
    else:
        d[kod] = []
    d[kod]+=[i]
# print(d)
print(*sorted(d.items()))

n = input().split()
d = dict([(x[:2], [i for i in n if x[:2] == i[:2]]) for x in n])
print(*sorted(d.items()))
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
