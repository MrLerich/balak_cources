'''
Подвиг 3. Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.

Sample Input:

8 11 12 1
9 4 36 -4
1 12 49 5
Sample Output:

1 -4 5
'''

# Создаем пустой список
lst = []
# В список вкладываем другие списки
lst.append(list(map(int, input().split())))
lst.append(list(map(int, input().split())))
lst.append(list(map(int, input().split())))
# Выводим последние цифры из каждого вложенного списка
print(f"{lst[0][-1]} {lst[1][-1]} {lst[2][-1]}")




# s1=list(map(int, input().split()))
# s2=list(map(int, input().split()))
# s3=list(map(int, input().split()))
# lst = [s1, s2, s3]
# print(lst[0][-1], lst[1][-1], lst[2][-1])
# # st1 = list(map(int,input().split()))
# # st2 = list(map(int,input().split()))
# # st3 = list(map(int,input().split()))
# # print(*[st1[-1],st2[-1],st3[-1]]) #упростил немног


# print(*[input().split()[-1] for _ in range(3)])