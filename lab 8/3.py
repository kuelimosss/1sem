# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 3: Найти столбец, имеющий определённое свойство по варианту
# Вариант 2: Наименьшее количество отрицательных элементов.

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

#Рассматриваем матрицу, как бы переворачивая ее
min_negative = line_count
column_num = -1
for j in range(column_count):
    count_negative = 0
    for i in range(line_count):
       if matr[i][j] < 0:
           count_negative += 1
    if count_negative < min_negative:
        min_negative = count_negative
        column_num = j
        
print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print('----------------------------')

if column_num == -1:
    print("Не нашлось ни одного столбца с отрицательными элементами")
else:
    print("Наибольшее количество отрицательных элементов в {:d}-ом столбце".format(column_num))
        

