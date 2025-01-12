# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задачи 6: Дана матрица символов. Преобразовать её следующим образом: заменить все согласные латинские букв на заглавные, 
# а все гласные латинские буквы на строчные. Вывести матрицу до преобразования и после.

line_count,column_count = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())
matrix= []
for i in range(line_count):
    row = []
    for j in range(column_count):
        elem = input("Введите {}-ый элемент {}-ой строчки: ".format(j,i))
        row.append(elem)
    matrix.append(row)

output_place = 0
for i in range (line_count):
    for j in range (column_count):
        if len(str(matrix[i][j])) > output_place:
            output_place= len(str(matrix[i][j]))

print("Исходная матрица ")
for i in range (line_count):
    for j in range (column_count):
        print("{:>{}}".format(matrix[i][j],output_place),end='|||')
    print()

# в кодировке unicode буквы от a до z  имеют значение от 
# 97 до 122, а заглавные от 65 до 90, тогда разница между
# соответственными буквами = 32
for i in range (line_count):
    for j in range (column_count):
        if len(str(matrix[i][j])) > output_place:
            output_place= len(str(matrix[i][j]))
        modified_elem = str(matrix[i][j])
        if matrix[i][j] not in 'eyuioa' and 97 <= ord(matrix[i][j]) <= 122:
            modified_elem = chr(ord(matrix[i][j])-32)
        elif matrix[i][j]  in 'EYUIOA':
            modified_elem = chr(ord(matrix[i][j])+32)

print("Измененная матрица ")
for i in range (line_count):
    for j in range (column_count):
        print("{:>{}}".format(matrix[i][j],output_place),end='|||')
    print()

# print(*arr, sep  = ', ')