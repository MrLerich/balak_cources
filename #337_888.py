'''

Подвиг 9. Вводится список названий городов в одну строчку через пробел.
Перебрать все эти названия с помощью цикла for и определить,
начинается ли название следующего города на последнюю букву предыдущего города в списке.
Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.

Sample Input:

Москва Астрахань Новгород Димитровград Душанбе

'''
# 1
lst = [city.rstrip("ьъы") for city in input().lower().split()]
for i in range(1, len(lst)):
    if lst[i - 1][-1] != lst[i][0]:
        print("НЕТ")
        break
else:
    print("ДА")

# 2
# import sys  # Импортирую библиотеку
#
# # считывание списка из входного потока
# list_word = input().lower().split()
# result = 'ДА'  # Переменная с флагом ДА
# list_num = []  # Пустой список
# for i in range(0, int(len(list_word) - 1)):  # Перебираю города
#     word_1 = list_word[i].rstrip("ьъы")[-1]  # берем слово из списка удаляем с права все буквы rstrip("ьъы")
#     # переводим все буквы в нижний регистр и берем последнюю букву [-1]
#     word_2 = list_word[i + 1][
#              0:1]  # берем следующие по индексу слово из списка, переводим его в нижний регистр и берем первую букву
#
#     if word_1 == word_2:  # Если буквы одинаковые
#         result = 'ДА'  # Выводим ДА
#     else:  # Иначе
#         result = 'НЕТ'  # Выводим НЕТ
#         break
# print(result)


# # 3
# data = input().lower().split()
# result = 'ДА'
# for i in range(1, len(data)):
#     if data[i][0] != data[i - 1].rstrip("ьъы")[-1]:
#         result = 'НЕТ'
# print(result)


# 4

cities = [i for i in input().lower().split()]
exc = ['ь', 'ъ', 'ы']
count = 0
for i in range(0, len(cities) - 1):
    if cities[i][-1] == cities[i + 1][0]:
        count += 1
    else:
        if cities[i][-1] in exc:
            if cities[i][-2] == cities[i + 1][0]:
                count += 1
if count == len(cities) - 1:
    print('ДА')
else:
    print('НЕТ')
