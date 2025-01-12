from math import cos
maxx = -(10**10)
minn = 10**10
xstart = float(input("Введите начальное значение аргумента х: "))
xend = float(input("Введите конечное значение аргумента х: "))
func_step = float(input("Введите шаг для вывода значений функции: "))

while func_step < 0:
    print("Шаг не может быть отрицательным")
    func_step = float(input("Введите шаг для вывода значений функции: "))

for i in range (int((xend - xstart)/ func_step) + 1):
    x = xstart + i * func_step
    y = cos(x)

    if y > maxx:
        maxx = y
    if y < minn:
        minn = y
symbols = 50
interval = (maxx - minn) / symbols


half = minn + (abs(maxx-minn)) / 2
print(' '*8+'{:5.3f}'.format(minn)+' '*(int(symbols/2)-5)+'{:5.3f}'.format(half)+' '*(int(symbols/2)-5)+'{:5.3f}'.format(maxx))

if minn < 0 and maxx > 0:
    for i in range(symbols):
        if minn + (i * interval) <= 0  < minn + ((i+1) * interval):
            id0 = i
            break
else:
    id0 = 0 

for i in range (int((xend - xstart)/ func_step) + 1):
    x = xstart + i * func_step
    y = cos(x)
    for j in range(symbols):
        if  y <= (minn + ((j+1) * interval)):
            id_dot = j
            break
    if id0:
        if id_dot> id0:
            print('{:<7.2f}|'.format(x)," " * (id0),'|',sep='',end='')
            print( " " * (id_dot-id0-1),'*',sep='')
        elif id_dot < id0:
            print('{:<7.2f}|'.format(x)," " * (id_dot),'*',sep='',end='')
            print(" " * (id0-id_dot-1),'|',sep='')
        else:
            print('{:<7.2f}|'.format(x)," " * (id_dot),'*',sep='')
            

    else:
        print('{:<7.2f}|'.format(x), " " *(id_dot),'*',sep='')

# print(maxx,minn)










# for i in range (int((xend - xstart)/ func_step) + 1):
#     x = xstart + i * func_step
#     y = cos(x)+1
#     for i in range(1, symbols + 1):
#         if y < (i * interval):
#             print('{:<7.3g}|'.format(x), " " * (i-1),'*',sep='')
#             break

    

# print(minn,maxx)