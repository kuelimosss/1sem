# Лабораторная работа №8 “Матрицы. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 1: Найти строку, имеющую определённое свойство по варианту.
# Вариант 3: Наибольшее количество чётных элементов.

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
max_even = 0
line_num = -1
for i in range(column_count):
    count_even = 0
    for j in range(line_count):
        if matr[i][j] % 2 == 0:
            count_even += 1 
    # count_even = len([x for x in matr[i] if x % 2 == 0]) #считаем количество четных в строке
    if count_even > max_even:
        max_even = count_even
        line_num = i

print("Исходная матрица")
for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()
print('----------------------------')

if line_num == -1:
    print("Не нашлось ни одной строчки с четными элементами")
else:
    print("Наибольшее количество чётных элементов в {:d}-ой строчке".format(line_num))
        

        

    
