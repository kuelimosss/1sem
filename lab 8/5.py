# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 5: Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.

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

max_ = matr[0][1]
min_ = matr[1][0]

for i in range(1,line_count):
    for j in range(i+1,line_count):
            max_ = max(max_,matr[i][j])

for i in range(1,line_count):
    for j in range(line_count-i,line_count):
            min_ = min(min_,matr[i][j])
            
print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print("Наибольший элемент над главной диагональю:{:d}".format(max_))
print("Наименьший элемент под побочной диагональю:{:d}".format(min_))