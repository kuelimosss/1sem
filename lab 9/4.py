# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задачи 4: Задана матрица D и массив I, содержащий номера строк, для которых 
# необходимо определить максимальный элемент. Значения максимальных 
# элементов запомнить в массиве R. Определить среднее арифметическое 
# вычисленных максимальных значений. Напечатать матрицу D, 
# массивы I и R, среднее арифметическое значение.

print("Введите матрицу D  ")
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

L = []
print("------------------------------------------")
print("Введите массив, ввод оканчивается символом '^' ")
el = input("Введите элемент списка (номер строки массива): ")
while el != '^' and len(L) < line_countD:
    if  int(el) < 0  or int(el) > line_countD -1:
        print("Введен неправильный номер строки массива ")
    elif int(el) in L:
        print("Введенный элемент уже есть в списке ")
    else:
        L.append(int(el))
    if len(L) == line_countD:
        break
    el = input("Введите элемент списка (номер строки массива): ")

output_place = 0
for i in range (line_countD):
    for j in range (column_countD):
        if len(str(matrixD[i][j])) > output_place:
            output_place= len(str(matrixD[i][j]))

R = []
s= 0
for i in L:
    max_elem = matrixD[i][0]
    for j in range(1, column_countD):
        if max_elem < matrixD[i][j]:
            max_elem = matrixD[i][j]
    R.append(max_elem)
    s += max_elem

middle = s / len(R)

print("Матрица D")
for i in range (line_countD):
    for j in range (column_countD):
        print("{:>{}d}".format(matrixD[i][j],output_place),end='')
    print()
print("Массив L")
print(*L)
print("Массив R")
print(*R)
print("Среднее арифметическое вычисленных максимальных значений: {}".format(middle))