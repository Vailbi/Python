print((lambda q,b: abs(q)+b)(-3,2))

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res



it = map(int, input().split())

lst = filter_lst(it,lambda x:x!=None)
print(*lst)

lst = filter_lst(it,lambda x:x<0)
print(*lst)

lst = filter_lst(it,lambda x:x>=0)
print(*lst)

lst = filter_lst(it,lambda x:3<=x<=5)
print(*lst)