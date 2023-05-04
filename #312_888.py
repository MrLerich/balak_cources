'''

Подвиг 4. Вводится список названий городов в одну строчку через пробел. Определить, что в этом списке все города имеют длину более 5 символов. Реализовать программу с использованием цикла while и оператора break. Вывести ДА, если условие выполняется и НЕТ - в противном случае.

Sample Input:

Самара Ульяновск Новгород Воронеж

'''




city = list(map(str, input().split()))
i = 0
ans = 'ДА'

while i < len(city):
    if len(city[i]) < 6:
        ans = 'НЕТ'
        break
    else:
        i += 1
print(ans)
#
# print(('НЕТ', 'ДА')[len(min(input().split(), key=len)) > 5])
'''
key - это доп. параметр фунции min, определяющий функцию, которая будет применена к каждому элементу списка 
(или другой перечисляемой последовательности переданной функции min) перед сравнением с другим элементов в процессе 
поиска минимального значения. В данном примере, вместо самих имен городов будут сравниватся их длины, поэтому будет 
выбран город с самым коротким именем.
'''


# city = input().split()
# i = 0
# while i < len(city):
#     if len(city[i]) < 5:
#         print('НЕТ')
#         break
#     i += 1
# else:
#     print('ДА')


# print(('НЕТ', 'ДА')[all(len(w) > 5 for w in input().split())])

'''
это от чего тебя так пробрало на хаха? Все таки нужно внимательнее читать комментарии других людей, прежде чем хохотать. 
Факты:

('НЕТ', 'ДА') - это кортеж из двух элеметов. Девушка совершенно права.

Функция all останавливает обход досрочно при первом невыполненом условии, поэтому она продуктивнее 
чем функция min в большинстве случаев.

Функции filter и map в принципе могут быть использованы вместо генератора длин слов, потому что они тоже являются 
объектами-генераторами и значит не обходят лишний раз всю последовательность 
а генерируют длины лениво, по запросу функции all.

По моему мнению, даже если человек ошибся (что в данном случае не произошло), он все равно заслуживает уважения 
и поддержки. Обратная связь это очень важная и полезная штука. Я сам тоже иногда ошибаюсь, а поправки и замечания 
других помогают это обнаружить и сделать выводы. Но делать замечания и поправки следует 
в позитивном, созидательном ключе. 
'''