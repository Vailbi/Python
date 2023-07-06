# # put your python code here
# t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
#      'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
#      'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}
#
#
# def Email(x):
#     if '@' in x and '.' in x and x.count('@') == 1:
#         for i in x:
#             if i in t:
#                 continue
#             else:
#                 print("НЕТ")
#                 exit()
#         print('ДА')
#     else:
#         print("НЕТ")
#
#
# mail = input()
#
# Email(mail)
#

# ЗАПОМНИ!!

# def Chet(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# ^^^^^^^ это ровнозначно нижнему
# def is_even(n):
#     return not n % 2


def City_prnt(x):
    return x, len(x)


# num = list(map(int,input().split()))
a,b = int(input()),int(input())
print(a,b)