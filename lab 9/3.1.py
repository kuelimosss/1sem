# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задачи 3: Даны две матрицы A и B, в которых количество столбцов одинаково.
# Подсчитать для каждого столбца матрицы А количество элементов, больших
# среднего арифметического элементов соответствующего столбца матрицы В.
# Вывести полученные значения. Затем преобразовать матрицу В путем
# умножения всех элементов столбца матрицы на посчитанное для этого столбца
# значение, если оно ненулевое. Вывести преобразованную матрицу в виде матрицы.

print("Введите матрицу А  ")
#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matrixA = [list(map(int,input("Введите 0-ую строчку матрицы A: ").split()))]
column_count = len(matrixA[0])
line_countA = 0
while True:
    line_countA += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы A: ".format(line_countA)).split()))
    if line == [00]:#Выход из цикла
        break
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку матрицы A: ".format(line_countA)).split()))
    matrixA.append(line)

print("Введите матрицу B  ")
#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")

matrixB = [list(map(int,input("Введите 0-ую строчку матрицы B: ").split()))]
line_countB = 0
while len(matrixB[0]) != column_count:
    print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
    matrixB = list(map(int,input("Введите {:d}-ую строчку матрицы B: ".format(line_countB)).split()))

while True:
    line_countB += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы B: ".format(line_countB)).split()))
    if line == [00]:#Выход из цикла
        break
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку матрицы B: ".format(line_countB)).split()))
    matrixB.append(line)

n = column_count

output_place = 0
for i in range (line_countA):
    for j in range (n):
        if len(str(matrixA[i][j])) > output_place:
            output_place= len(str(matrixA[i][j]))
for i in range (line_countB):
    for j in range (n):
        if len(str(matrixB[i][j])) > output_place:
            output_place= len(str(matrixB[i][j]))

print("Матрица A")
for i in range (line_countA):
    for j in range (n):
        print("{:>{}d}".format(matrixA[i][j],output_place+2),end='')
    print()

print("Матрица B")
for i in range (line_countB):
    for j in range (n):
        print("{:>{}d}".format(matrixB[i][j],output_place+2),end='')
    print()

otv = []
for j in range(n):
    sB = 0
    for i in range(line_countB):
        sB += matrixB[i][j]
    middleB = sB / line_countB
    count_A = 0
    for i in range(line_countA):
        if matrixA[i][j] > middleB:
            count_A += 1
    otv.append(count_A)     
    if count_A != 0:
        for i in range(line_countB):
                matrixB[i][j] *= count_A

print()
print("Измененная матрица B")
for i in range (line_countB):
    for j in range (n):
        print("{:>{}d}".format(matrixB[i][j],output_place+2),end='')
    print()
print()
print(*otv,sep=f'f{output_place+2}')