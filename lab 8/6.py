# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 6: Выполнить транспонирование квадратной матрицы

#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, матрица квадратная  ")
matr = [list(map(int,input("Введите 0-ую строчку матрицы: ").split()))]
column_count = len(matr[0])
line_count = 1
while line_count < column_count :
    line_count += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы: ".format(line_count-1)).split()))
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку: ".format(line_count)).split()))
    matr.append(line)

print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print('----------------------------')
for i in range(line_count):
    for j in range(i+1,line_count):
        matr[i][j],matr[j][i] = matr[j][i],matr[i][j]
print("Измененная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()