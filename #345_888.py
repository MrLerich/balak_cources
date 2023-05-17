'''

Большой подвиг 3. В виде строки записано арифметическое выражение, например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть разным.

Необходимо выполнить вычисление и результат отобразить на экране. Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
'''

text = input()  # .replace(' ', '').replace('-', '+-').split('+')
a = text.replace(' ', '')  # удаляем пробелы
print(a)
b = a.replace('-', '+-')  # добавляем + как флаг для разделения в списке
print(b)
c = b.split('+')  # разделяем по + в список
print(c)
print(sum(map(int, c)))  # text)))  # делаем каждый элт в списке интом

#
# first_operation = input()         # Получаю начальные данные
# str_middle = first_operation.replace('+', ' ').replace('-', ' ')  # Делаю строку из цифр разделяют ее пробелами
# list_number = list(str_middle.split())  # Делаю список из чисел
# sign_list = []                    # Делаю список
# for i in first_operation:         # Выбираю знаки сложения и вычитания
#     if i == '+' or i == '-':
#         sign_list.append(i)       # Сохраняю их в список знаков
# result = int(list_number[0])      # Сохраняю первое число в переменную  result
# for i in range(0, len(list_number) - 1): # Сохраняю первое число в переменную  result
#     if sign_list[i] == '+':
#         result = result + int(list_number[i + 1]) # Суммирую
#     else:
#         result = result - int(list_number[i + 1]) # Вычитаю
# print(result)


# (lambda x: print(sum(list(map(int, x.replace(' ', '').replace('-', '+-').split('+')))))if not x.startswith('-') else print(sum(list(map(int, x.replace(' ', '').replace('-', '+-')[1:].split('+'))))))(input())

# e = map(int, input().replace(' ', '').replace('+', ' +').replace('-', ' -').split())
# print(sum(e))

# print(eval(input()))

# exec(f"print({input()})")