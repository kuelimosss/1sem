# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задача 2: Повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
# затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не вводить. 
# Транспонирование не применять.

#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, матрица квадратная  ")
matrix = [list(map(int,input("Введите 0-ую строчку матрицы: ").split()))]
column_count = len(matrix[0])
line_count = 1
while line_count < column_count :
    line_count += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы: ".format(line_count-1)).split()))
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку: ".format(line_count)).split()))
    matrix.append(line)

n = column_count

output_place = 0
for i in range (n):
    for j in range (n):
        if len(str(matrix[i][j])) > output_place:
            output_place= len(str(matrix[i][j]))

print("Исходная матрица")
for row in matrix:
    for elem in row:
        print("{:>{}d}".format(elem,output_place+2),end='')
    print()

for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = temp

print("Матрица после поворота по часовой")
for row in matrix:
    for elem in row:
        print("{:>{}d}".format(elem,output_place+2),end='')
    print()

#поворот на 180 
for i in range(n):
    for j in range(n // 2):
        matrix[i][j], matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], matrix[i][j]
    
print("Матрица после поворота против часовой")
for row in matrix:
    for elem in row:
        print("{:>{}d}".format(elem,output_place+2),end='')
    print()