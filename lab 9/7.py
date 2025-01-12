# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задача 7: Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
# массива по большему измерению, индекс среза – середина размерности с
# округлением в меньшую сторону.

x,y,z = list(map(int, input("Введите измерения матрицы через пробел: ").split()))
while x < 1 or y < 1 or z < 1:
    x,y,z = list(map(int, input("Введите измерения  матрицы через пробел: ").split()))
matrix = []
for i in range(x):
    matrixx = []
    for j in range(y):
        row = list(map(int,input("Введите строку {} матрицы {}: ".format(j,i+1)).split()))
        while len(row) != z:
            print("Количество элементов строки не равно {}".format(z))
            row = list(map(int,input("Введите строку {} матрицы {}: ".format(j,i+1)).split()))
        matrixx.append(row)
    matrix.append(matrixx)

# for u in range(x):
#     for i in range(y):
#         for j in range(z):
#              print('{:>6g}'.format(matrix[u][i][j]), end=' ')
#         print()
#     print('padsfkyadskhu-')
if x > y and x > y:
    for i in range(y):
        for j in range(z):
            print('{:>6g}'.format(matrix[x//2][i][j]), end=' ')
        print()
elif y > x and y > z:
    for i in range(x):
        for j in range(z):
            print('{:>6g}'.format(matrix[i][y//2][j]), end=' ')
        print()
else:
    for i in range(x):
        for j in range(y):
            print('{:>6g}'.format(matrix[i][j][z//2]), end=' ')
        print()


