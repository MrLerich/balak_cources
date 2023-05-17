'''Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых позициях, единиц
(см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали.
То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
Sample Output:

ДА
'''
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
n = len(lst_in) - 1 # без учета последней

for i in range(n):
    for j in range(n):
        if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
            print('НЕТ')
            break
    else:
        continue
    break  # выход из внешнего цикца
else:
    print('ДА')



###########################
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
flag = True

for row in range(4):  # координаты строки (без учета последней)
    if not flag:  # Проверка на прерывание цикла
        break

    for col in range(4):  # координаты колонки (без учета последней)
        if not flag:  # Проверка на прерывание цикла
            break

        # считаем количество единиц в ближайшем окружении
        test_sum = sum(lst_in[row][col:col + 2] + lst_in[row + 1][col:col + 2])
        # останавливаем цикл, если единиц больше
        if test_sum > 1:
            flag = False

print(('НЕТ', 'ДА')[flag])

########################################################
import sys
m = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
for i in range(4):
    for j in range(4):
        if m[i][j] + m[i + 1][j] + m[i][j + 1] + m[i + 1][j + 1] >= 2:
            print("НЕТ")
            sys.exit()
print('ДА')

#############################################################


# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in: list = [list(map(int, x.strip().split())) for x in s]
# # здесь продолжайте программу (используйте список lst_in)
#
# # lst_in = [[1, 0, 0, 0, 0],
# #           [0, 0, 1, 0, 1],
# #           [0, 0, 0, 0, 0],
# #           [0, 1, 0, 1, 0],
# #           [0, 0, 0, 0, 0]]
#
# string_matrix = len(lst_in[0])
# flag = True
# lst_in = [[0] * string_matrix] + (lst_in) + [[0] * string_matrix]  # Добавляем строки вверх и вниз матрицы
# for i in range(len(lst_in)):  # Добавляем столбцы
#     lst_in[i].insert(0, 0)  # Первый столбец матрицы
#     lst_in[i].append(0)  # Последний столбец матрицы
# for index_str, value in enumerate(lst_in):  # Прохожу по строкам и сохраняю данные в переменную value, индексы index_str
#     if flag == True:  # Ставлю флаг в True
#         for index_positon, value_str in enumerate(value):  # Ставлю флаг в True
#             if value_str == 1:  # Если встречаю 1 в матрице начинаю проверять на соприкосновение с другими единицами
#                 if (lst_in[index_str][index_positon + 1] + value_str + lst_in[index_str][
#                     index_positon - 1]) > 1:  # Слева или справа
#                     flag = False
#                     break
#                 if 1 in lst_in[index_str - 1][index_positon - 1: index_positon +1]: # Верхний ряд
#                     flag = False
#                     break
#                 if 1 in lst_in[index_str + 1][index_positon: index_positon + 1]:  # Нижний ряд
#                     flag = False
#                     break
#                     # Случае нахождения прерываю поиск, flag ставлю в False
#                 else:
#                     flag = True  # Иначе flag = True
#     else:
#         break  # Если флаг в положение False прерываю поиск.
# if flag:
#     print("ДА")
# else:
#     print("НЕТ")

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in: list = [list(map(int, x.strip().split())) for x in s]
# # здесь продолжайте программу (используйте список lst_in)

lst_in = [[1, 0, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]

string_matrix = len(lst_in[0])
flag = True
lst_in = [[0] * string_matrix] + (lst_in) + [[0] * string_matrix]  # Добавляем строки вверх и вниз матрицы
for i in range(len(lst_in)):  # Добавляем столбцы
    lst_in[i].insert(0, 0)  # Первый столбец матрицы
    lst_in[i].append(0)  # Последний столбец матрицы
for index_str, value in enumerate(lst_in):  # Прохожу по строкам и сохраняю данные в переменную value, индексы index_str
    if flag == True:  # Ставлю флаг в True
        for index_positon, value_str in enumerate(value):  # Ставлю флаг в True
            if value_str == 1:  # Если встречаю 1 в матрице начинаю проверять на соприкосновение с другими единицами
                if (lst_in[index_str][index_positon + 1] + lst_in[index_str][
                    index_positon - 1]) > 0 or 1 in lst_in[index_str - 1][index_positon - 1: index_positon + 1] or 1 in \
                        lst_in[index_str + 1][index_positon: index_positon + 1]:
                    '''проверяю если боковые от позиции имеют 1 , проверяю 1 в верхнем и нижнем ряду'''
                    flag = False
                    break
                else:
                    flag = True  # Иначе flag = True
# else:
#     break  # Если флаг в положение False прерываю поиск.
if flag:
    print("ДА")
else:
    print("НЕТ")
