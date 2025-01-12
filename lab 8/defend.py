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
p_negative = []

for i in range (line_count):
    for j in range (column_count):
        print("{:>10d}".format(matr[i][j]),end='')
    print()

for i in range(line_count):
    count_negative = 0
    p = 1
    for j in range(column_count):
        if matr[i][j] < 0:
            count_negative += 1 
            p = p * matr[i][j]
    if count_negative > 0: 
        p_negative.append(p)
    else:
        p_negative.append(0)
print(p_negative)
print(len([x for x in p_negative if x==0]))

    