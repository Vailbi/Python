# import time
#
#
# def test_time(func):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = func(*args, **kwargs)
#         et = time.time()
#         dt = et - st
#         print(f'вермя работы {func.__name__} = {dt}') # {func.__name__} имя функции
#         return res
#
#     return wrapper
#
#
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# get_nod = test_time(get_nod)
# res = get_nod(6, 1004546)
# print(res)


# def func_show(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         print(f'Площадь прямоугольника: {res}')
#         return res
#     return wrapper
#
#
# @func_show
# def get_sq(width, height):
#     return width*height
#
#
#
# get_sq(8,11)
# get_sq = func_show(get_sq)
# get_sq(8,11)

# def set_menu(func):
#     def wrapper(*args, **kwargs):
#         menu = func(*args)
#         for num, val in enumerate(menu, 1):
#             print(f"{num}. {val}")
#         return menu
#
#     return wrapper
#
#
# @set_menu

#
# get_menu('qwe dfg vb dg')

def create_dict(func):
    def wrapper(a,b):
        key = func(a,b)
        d = dict(zip(key[0], key[1]))
        # print(*sorted(d.items()))
        return d

    return wrapper


# @create_dict
# def get_menu(s):
#     return s.split()
#
#
# @create_dict
# def get_list(line_keys, line_values):
#     return [line_keys.split(), line_values.split()]
#
#
#
# d = get_list('house river tree car', 'дом река дерево машина')
# print(*sorted(d.items()))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
#      ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}
#
# def format_string(func):
#     def wrapper(*args):
#         txt = func(*args)
#         while '--' in txt:
#             txt = txt.replace('--', '-')
#         return txt
#     return wrapper
#
#
# @format_string
# def translate(text):
#     res = ''.join([t.get(i) if i in t.keys() else i for i in text.rstrip().lstrip().lower()])
#     return res.rstrip('-').lstrip('-')
#
# print(translate("    Python -----    - Это : ;.,_ круто! --- "))


def get_arg_decorator(start = 5):
    def decorator(func):
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)+start
            return res
        return wrapper
    return decorator


@get_arg_decorator(start=5)
def summa(num):
    return sum(list(map(int, num.split())))


print(summa('1 2 3'))

