d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
def get_line_list(d,a=[]):
    if len(a)!=len(d):
        for i in d:
            if type(i) != list:
                a.append(i)
            else:
                get_line_list(i, a)
    return a


# print(get_line_list(d))


# метод сортировки слиянием
l = [int(i) for i in input().split()]


def merge_two_lists(a, b):
    res = []
    while a and b:
        res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
    return res + a + b


def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    a, b = l[:mid], l[mid:]
    return merge_two_lists(merge_sort(a), merge_sort(b))


print(*merge_sort(l))
