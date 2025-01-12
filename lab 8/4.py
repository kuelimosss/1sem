# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 4: Переставить местами столбцы с максимальной и минимальной суммой элементов.

#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matr = [list(map(int,input("Введите 0-ую строчку матрицы: ").split()))]
column_count = len(matr[0])
line_count = 0
while True:
    line_count += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы: ".format(line_count)).split()))
    if line == [00]: #Выход из цикла 
        break
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку: ".format(line_count)).split()))
    matr.append(line)


#задаем максимальную и минимальную сумму первым столбцом

s = 0 
for i in range(line_count):
    s += matr[i][0]
    
min_ = s
max_ = s
column_num_max = -1
column_num_min = -1


#Рассматриваем матрицу, как бы переворачивая ее
for j in range(1,column_count):
    s = 0 
    for i in range(line_count):
        s += matr[i][j] 
    if s < min_:
        min_ = s
        column_num_min = j
    if s > max_:
        max_ = s
        column_num_max = j
print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print('----------------------------')
for i in range(line_count):
    matr[i][column_num_min],matr[i][column_num_max] = matr[i][column_num_max], matr[i][column_num_min]
print('Изменённа матрица')
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()