from string import ascii_lowercase, ascii_uppercase

from re import match

# is_email = lambda email: match('\w+@\w+\.\w+', email)
# print(*filter(is_email, input().split()))

chars = ascii_lowercase + ascii_uppercase

email = input().split()


def chek_mail(arr):
    if arr.count('@') == 1 and arr.count('.') == 1:
        flag = True
        for i in arr[:arr.index('@')]:
            if i not in chars + '_@1234567890':
                flag = False
    else:
        flag = False
    return flag


res = filter(chek_mail, email)
print(*res)
