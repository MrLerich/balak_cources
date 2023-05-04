'''

Подвиг 5. Вводится список имен студентов в одну строчку через пробел.
Определить, что хотя бы одно имя в этом списке начинается
и заканчивается на ту же самую букву (без учета регистра).
Реализовать программу с использованием цикла while и оператора break.
Вывести ДА, если условие выполняется и НЕТ - в противном случае.

Sample Input:

Петр Анна Иван Сергей Михаил Федор

'''

name = list(map(str, input().lower().split()))

i = 0
ans = 'НЕТ'

while i < len(name):
    if name[i][0] == name[i][-1]:
        ans = 'ДА'
        break
    i += 1
print(ans)

# names = input().split()
# res, count = 'НЕТ', len(names)
# while count:
#     count -= 1
#     if names[count][0].lower() == names[count][-1].lower():
#         res = 'ДА'
#         break
# print(res)

# print(('НЕТ', 'ДА')[any(i[0] in i[-1] for i in input().lower().split())])

# print('ДА' if any(map(lambda name: name[0] == name[-1], input().lower().split())) else 'НЕТ')

# students = list(map(lambda x: x.lower(), input().split()))
# i = 0
# flag = False
# while i < len(students):
#     if students[i][0] == students[i][-1]:
#         flag = True
#         break
#     i += 1
# print(['НЕТ', 'ДА'][flag])
