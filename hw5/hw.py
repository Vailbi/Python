# def RLE_Algorithm (text):
#     result = ''
#     count = 1
#     for index, symbol in enumerate(text):
#         if index < len(text)-1:
#             if symbol == text[index+1]:
#                 count += 1
#                 pre_result = str(symbol + str(count))
#                 final_count = count
#                 print(pre_result)
#             else:
#
#                 count = 1
#                 result += pre_result
#
#         elif symbol != text[len(text)-1]:
#             result += symbol+str(final_count)
#             break
#         else:
#             result += symbol
#     return result
#
# test = input()
# print(RLE_Algorithm(test))
#


# p = [0] * 10
# count = 0
# while count < 6:
#     index = int(input())
#     if p[index] == 0:
#         p[index] = 1
#         count += 1
#     elif p[index] == 1:
#         count += 0
# print(*p)

# Подвиг 9. Вводится список названий городов в одну строчку через пробел.
# Перебрать все эти названия с помощью цикла for и определить, начинается ли название следующего города на
# последнюю букву предыдущего города в списке. Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая
# с конца буква.
# Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.

# city = input().split()
# result = ''
# for i in range(len(city)-1):
#     if city[i][-1] in ['ь', 'ъ', 'ы']:
#         if city[i][-2] == city[i+1][0].lower():
#             result = "ДА"
#         else:
#             result = "НЕТ"
#             break
#     else:
#         if city[i][-1] == city[i+1][0].lower():
#             result = "ДА"
#         else:
#             result = "НЕТ"
#             break
# print(result)

# lst = [city.rstrip("ьъы") for city in input().split()]
# for i in range(1,len(lst)):
#     if lst[i-1][-1] != lst[i][0].lower():
#         print("НЕТ")
#         break
# else:
#     print("ДА")
# версия два

# Подвиг 10. Вводится натуральное число n.
# Вычислить сумму всех натуральных чисел меньше n, которые кратны или 3 или 5. Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.

# print(sum(i for i in range(int(input())) if i % 3==0 or i % 5 ==0))



# search = list(i for i in range(1, int(input())))
# num = int(input())
# print(*search)
# print(search.count(num))


size = int(input())
search = list(i for i in range(size))
num = int(input())
result = 0
if num > len(search):
    result = search[-1]
elif num >= 0 and num <= size:
    result = f'{num-1} или {num+1}'
elif num < 0:
    result = 0
print(*search)
print(result)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai