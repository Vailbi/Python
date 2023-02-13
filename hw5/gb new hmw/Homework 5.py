# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# a = int(input())
# b = int(input())
# def Stepen(x,y):
#     while y != 1:
#         return Stepen(x,y-1)*x
#     return x
# print(Stepen(a,b))
#

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
a = int(input())
b = int(input())
def Summa(x,y):
    while y != 0:
        return Summa(x+1,y-1)
    return x
print(Summa(a,b))