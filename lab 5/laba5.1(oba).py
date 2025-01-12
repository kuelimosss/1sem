#Лабораторная работа №5  “График”
#Функция: r = 1.23 * x**5 - 2.52 * x**4 - 16.1 * x**3 + 17.3 * x**2
#Шагаев Андрей ИУ7-14Б
#Вариант №4
eps = 1e-4
maxx = 10**-10
minn = 10**10
xstart = float(input("Введите начальное значение аргумента х: "))
xend = float(input("Введите конечное значение аргумента х: "))
func_step = float(input("Введите шаг для вывода значений функции: "))
#Вывод таблицы значений
while func_step < 0:
    print("Шаг не может быть отрицательным")
    func_step = float(input("Введите шаг для вывода значений функции: "))

print('---------------------------------')
for i in range (int((xend - xstart)/ func_step) + 1):
    x = xstart + i * func_step
    r = 1.23 * x**5 - 2.52 * x**4 - 16.1 * x**3 + 17.3 * x**2

    #Определение максимального и минимального значений функции
    if r > maxx:
        maxx = r
    if r < minn:
        minn = r

    print('{:<7.2f} |{:^8.5f}|'.format(x, r))
print('---------------------------')

#Запрос ввода засечек
strokes = int(input("Введите количество засечек от 4 до 8: "))
while not ( 4 <= strokes <= 8 ):
    print("Введено неправильное число засечек")
    strokes = int(input("Введите количество засечек от 4 до 8: "))

#Вывод оси Oy
symbols = 120
delta = (maxx - minn) / (strokes - 1) # числовая разница между засечками
step = round((symbols - (6 * (strokes - 1))) / (strokes - 1)) #пробелов между засечками
print(" " * 7, "{:.3g}".format(minn)," " * step,end='')
for number in range (1, (strokes + 1) - 2):
    print("{:6.3g}".format(minn+ number * delta)," " * step,end='')
print("{:6.3g}".format(maxx))

# 8 символов с | + symbols = ширина строки
#Вывод графика
interval = (maxx - minn) / symbols
if minn < 0 and maxx > 0:
    for i in range(symbols):
        if minn + (i * interval) <= 0  < minn + ((i+1) * interval):
            q = i
            break
else:
    q = 0 


for i in range (int((xend - xstart)/ func_step) + 1):
    x = xstart + i * func_step
    r = 1.23 * x ** 5 - 2.52 * x ** 4 - 16.1 * x ** 3 + 17.3 * x ** 2
    for j in range(symbols):
        if minn + (j * interval) <= (r -eps) < minn + ((j+1) * interval):
            if abs(x-1.05) < eps:
                print(minn + (j * interval),minn + ((j+1) * interval))
            w = j
            break
    if q:
        if w > q:
            print('{:<7.2f}|'.format(x)," " * (q),'|',sep='',end='')
            print( " " * (w-q-1),'*',sep='')
        elif w < q:
            print('{:<7.2f}|'.format(x)," " * (w),'*',sep='',end='')
            print(" " * (q-w-1),'|',sep='')
        else:
            print('{:<7.2f}|'.format(x)," " * (w),'*',sep='')
            

    else:
        print('{:<7.2f}|'.format(x), " " * w,'*',sep='')

print("Значение r_min / r_max = {:1g}".format(minn / maxx))
print(interval)






















    # is_zero = 0
    # is_dot = 0
    # for i in range(1, symbols + 1):
    #     if r < 0:
    #         if (r - eps ) < (minn + (i * interval)) and is_dot == 0:
    #             print('{:<7.2f}|'.format(x), " " * (i-1),'*',sep='',end='')
    #             id_prev = i
    #             is_dot = 1
    #         if 0 < (i * interval) and is_zero == 0 and is_dot == 1:
    #             print(" " * (i-1-id_prev),'|',sep='')
    #             is_zero = 1
    #     if r > 0:
    #         if 0 < (minn + (i * interval)) and is_zero == 0:
    #             print('{:<7.2f}|'.format(x), " " * (i-1),'|',sep='',end='')
    #             is_zero = 1
    #             id_prev= i
    #         if (r - eps ) < (i * interval) and is_dot == 0 and is_zero == 1:
    #             print(" " * (i-1-id_prev),'*',sep='')
    #             is_dot = 1