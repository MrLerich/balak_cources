'''
Имеется список базовых нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел. Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'. Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).

Sample Input:

1 6 7
Sample Output:

#до ля си
'''

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

# ввод номеров нот
a, b, c = map(int, input().split())

# формирование строки нот с учетом символов диеза
result = "{} {} {} ".format(m[a-1] if a not in [1, 4] else "#" + m[a-1],
                            m[b-1] if b not in [1, 4] else "#" + m[b-1],
                            m[c-1] if c not in [1, 4] else "#" + m[c-1])

print(result)


# lst = map(int, input().split())
#
# print(*map(lambda x: f'#{m[x-1]}' if x in [1,4] else m[x-1], lst))
