# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 2: Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов.

#Построчный ввод элементов, проверка правильности ввода длины каждой строки 
print("Ввод матрицы осуществляется построчно, оканчивается '00' ")
matr = [list(map(int,input("Введите 0-ую строчку матрицы: ").split()))]
column_count = len(matr[0])
line_count = 0
while True:
    line_count += 1
    line = list(map(int,input("Введите {:d}-ую строчку матрицы: ".format(line_count)).split()))
    if line == [00]:#Выход из цикла
        break
    while len(line) != column_count:
        print("Вы ввели строчку, длиной {:d}, введите строчку длиной {:d}: ".format(len(line),column_count))
        line = list(map(int,input("Введите {:d}-ую строчку: ".format(line_count)).split()))
    matr.append(line)

# Строка - массив в нашей матрице
max_negative = -1
min_negative = column_count
line_num_min = line_num_max = -1
for i in range(column_count):
    count_negative = 0
    for j in range(line_count):
        if matr[i][j] < 0:
            count_negative += 1 
    # count_negative = len([x for x in matr[i] if x < 0]) #подсчет количества отрицательных
    if count_negative > max_negative:
        max_negative = count_negative
        line_num_max = i
    if count_negative < min_negative:
        min_negative = count_negative
        line_num_min = i

print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print('----------------------------')
if line_num_max != line_num_min:
    matr[line_num_min],matr[line_num_max] = matr[line_num_max], matr[line_num_min] #меняем местами найденные строки

print('Изменённа матрица')
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()