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

print('---------------------------------')
for i in range (int((xend - xstart)// func_step) + 1):
    x = xstart + i * func_step
    r = 1.23 * x**5 - 2.52 * x**4 - 16.1 * x**3 + 17.3 * x**2

    #Определение максимального и минимального значений функции
    if r > maxx:
        maxx = r
    if r < minn:
        minn = r

    print('{:<7.2f} |{:^8.5f}|'.format(x, r))
print('---------------------------')

print(maxx,minn)
#Запрос ввода засечек
strokes = int(input("Введите количество засечек от 4 до 8: "))
while not ( 4 <= strokes <= 8 ):
    print("Введено неправильное число засечек")
    strokes = int(input("Введите количество засечек от 4 до 8: "))

#Вывод оси Oy
symbols = 120
delta = (maxx - minn) / (strokes - 1) # числовая разница между засечками
step = round((symbols - (6 * (strokes - 1))) / (strokes - 1)) #пробелов между засечками
print(" " * 7, "{:1g}".format(minn)," " * step,end='')
for number in range (1, (strokes + 1) - 2):
    print("{:6.3f}".format(number * delta)," " * step,end='')
print("{:6.3f}".format(maxx))

# 8 символов с | + symbols = ширина строки
#Вывод графика
interval = (maxx - minn) / symbols

for i in range (int((xend - xstart)// func_step) + 1):
    x = xstart + i * func_step
    r = 1.23 * x ** 5 - 2.52 * x ** 4 - 16.1 * x ** 3 + 17.3 * x ** 2
    for i in range(1, symbols + 1):
        if (r - eps )< (i * interval):
            print('{:<7.2f}|'.format(x), " " * (i-1),'*',sep='')
            break
print("Значение r_min / r_max = {:1g}".format(minn / maxx))