# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задачи 5: Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и В. Вывести все матрицы в виде матриц.

print("Введите матрицу А  ")
#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matrixA = [list(map(int,input("Введите 0-ую строчку матрицы A: ").split()))]
column_countA = len(matrixA[0])
line_countA = 0
while True:
    line_countA += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы A: ".format(line_countA)).split()))
    if line == [00]:#Выход из цикла
        break
    while len(line) != column_countA:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_countA))
        line = list(map(int,input("Введите {:d}-ую строчку матрицы A: ".format(line_countA)).split()))
    matrixA.append(line)

print("Введите матрицу B  ")
#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matrixB = [list(map(int,input("Введите 0-ую строчку матрицы B: ").split()))]
column_countB = len(matrixB[0])
line_countB = 1
while line_countB < column_countA:
    line_countB += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы B: ".format(line_countB - 1)).split()))
    while len(line) != column_countB:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_countB))
        line = list(map(int,input("Введите {:d}-ую строчку матрицы B: ".format(line_countB - 1)).split()))
    matrixB.append(line)
#умножение матриц возможно, только если количество столбцов первой 
#ранво количетсву строк второй 
#column_countA = line_countB
matrixC = [[0] * column_countB for i in range(line_countA)]
output_place = 0
for i in range(line_countA):
    for j in range(column_countB):
        el = 0
        for k in range(column_countA):
            el += matrixA[i][k] * matrixB[k][j]
        matrixC = el 
    matrixC.append(row)

print("Матрица A")
for i in range (line_countA):
    for j in range (column_countA):
        print("{:>10d}".format(matrixA[i][j]),end='')
    print()

print("Матрица B")
for i in range (line_countB):
    for j in range (column_countB):
        print("{:>10d}".format(matrixB[i][j]),end='')
    print()

print("Матрица C")
for i in range (len(matrixC)):
    for j in range (len(matrixC[0])):
        print("{:>10d}".format(matrixC[i][j]),end='')
    print()