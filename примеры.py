# перевод через встроенный транслятор shit + alt + T 
### сумма чисел в массиве больше 0 (The amount of numbers in the array is greater 0)
# Оставляй комментарии!!!
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#### инвертация элементов с - на + и наоборот 1 мой вариант 2ой с кодварса
def invert(lst):
    for i in range(0, len(lst)):
        if (lst[i] < 0):
            lst[i] = -(lst[i])
        else:
            lst[i] = -(lst[i])
    return lst


# def invert(lst):
# return [-x for x in lst]


##### показать первую цифру которая не идет по порядку
def first_non_consecutive(arr):
    not_consecutive = None
    for i in range(len(arr) - 1):
        if (arr[i] > 0):
            if (arr[i + 1] - arr[i] > 1):
                not_consecutive = arr[i + 1]
                break
        else:
            if (-(arr[i + 1]) - (-arr[i]) < -1):
                not_consecutive = arr[i + 1]
                break

    return not_consecutive

    #def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None


#### создание послдеовательности букв на примере accum("abcd") -> "A-Bb-Ccc-Dddd"
test = "abcdfkgkfjG"


def accum(s):  # сам способ
    for i in range(0, len(s)):
        if i == 0:
            result = s[i].upper()
        elif i < len(s):
            result += "-"
            result += s[i].upper().ljust(i + 1, s[i].lower())
        else:
            result += s[i].upper().ljust(i + 1, s[i].lower())
    return result



#### вывод среднего символа, если строка четная то два символа если нет то один
def get_middle(s):
    if len(s) % 2 == 0:
        x = len(s) // 2
        return (s[x-1:x+1])
    else:
        x = len(s) // 2
        return (s[x])

##### нахождения в массиве количества элементов больше нуля , и сумму отрицательных

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

##### найти сумму элементов aeiouAEIOU
def getCount(inputStr):
    print(inputStr)
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

##### замена днк atcg на tagc
def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])

##### вернуть строку где перевернуты слова больше 4 букв. на вход тоже строка 1)мое решение 2) лучшее
def spin_words(sentence):
    sentence = sentence.split(' ')

    for i in range(len(sentence)):
        if (len(sentence[i]) > 4):
            sentence[i] = sentence[i][::-1]

    return " ".join(sentence)

##### формат телефона (123) 156-4569 мощно
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)