print("Введите матрицу ")
#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matrixD = [list(map(int,input("Введите 0-ую строчку матрицы D: ").split()))]
column_countD = len(matrixD[0])
line_countD = 0
while True:
    line_countD += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы D: ".format(line_countD)).split()))
    if line == [00]:#Выход из цикла
        break
    while len(line) != column_countD:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_countD))
        line = list(map(int,input("Введите {:d}-ую строчку матрицы D: ".format(line_countD)).split()))
    matrixD.append(line)

print("Матрица D")
for i in range (line_countD):
    for j in range (column_countD):
        print("{:>10d}".format(matrixD[i][j]),end='')
    print()

max_ = float('-inf')
maxi = -1
maxj = -1
min_ = float('inf')
mini = -1
minj = -1
for i in range (line_countD):
    for j in range (column_countD):
        if matrixD[i][j] > max_:
            max_ = matrixD[i][j]
            maxi = i
            maxj = j
        if matrixD[i][j] < min_:
            min_ = matrixD[i][j]
            mini = i
            minj = j

newline = abs(maxi - mini)
newcolumn = abs(maxj - minj)

mini_range = min(maxi,mini)
minj_range = min(minj,maxj)

print("\nПодматрица D\n")
s = 0 
k = 0
for i in range(mini_range,mini_range+newline+1):
    for j in range(mini_range-1,minj_range+newcolumn+1):
            if matrixD[i][j] > 0:
                s += matrixD[i][j]
                k += 1
            print("{:>10d}".format(matrixD[i][j]),end='')
    print()

print("Среднее арифметическое положительных элементов подматрицы: ", s / k)