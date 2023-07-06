# from string import ascii_lowercase
# gen = (i+j for i in ascii_lowercase for j in ascii_lowercase)
# res = []
# # for i in range(50):
# #     res.append(next(gen))
# # print(*res)
# [print(next(gen), end= ' ') for _ in range(50)] # тоже самое что и сверху ЗАПОМНИТЬ


# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen = (cities[i%6] for i in range(10000000))
# [print(next(gen), end= ' ') for _ in range(20)]
a, b = map(int, input().split())
gen = ((0.5 * pow(i/100, 2) - 2.0) for i in range(a*100,b*100))
[print(round(next(gen),2), end= ' ') for _ in range(20)]