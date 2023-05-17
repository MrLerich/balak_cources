# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# # lst_in = [list(map(int, x.strip().split())) for x in s]
#
# # здесь продолжайте программу (используйте список lst_in)
lst_in = [[2, 3, 4, 5, 6],
          [3, 2, 7, 8, 9],
          [4, 7, 2, 0, 4],
          [5, 8, 0, 2, 1],
          [6, 9, 4, 1, 2]]
out = 'ДА'
for i in range(len(lst_in)):
    if out == 'НЕТ':
        break
    for j in range(i + 1, len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            out = 'НЕТ'
            break
else:
    out = 'ДА'

print(out)

# for row in lst_in:
#     for x in row:
#         print(x, end='\t')
#     print()
