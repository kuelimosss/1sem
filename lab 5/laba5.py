#Лабораторная работа №5  “График”
#Функция: r = 1.23 * x**5 - 2.52 * x**4 - 16.1 * x**3 + 17.3 * x**2
#Шагаев Андрей ИУ7-14Б
#Вариант №4
maxx = 10**-10
minn = 10**10
#Вывод таблицы значений
print('---------------------------------')
for x100 in range (-110, 15 , 5):
    x = x100/100
    r = 1.23 * x**5 - 2.52 * x**4 - 16.1 * x**3 + 17.3 * x**2

    #Определение максимального и минимального значений функции
    if r > maxx:
        maxx = r
    if r < minn:
        minn = r

    print('{:<7} |{:^8.5f}|'.format(x, r))
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
print(" " * 7, "{:1g}".format(minn)," " * step,end='')
for number in range (1, (strokes + 1) - 2):
    print("{:6.3f}".format(number * delta)," " * step,end='')
print("{:6.3f}".format(maxx))

# 8 символов с | + symbols = ширина строки
#Вывод графика
interval = (maxx - minn) / symbols
x = -1.1
print('{:<7}|'.format(x), " " * (step * (strokes - 1) + 6 * (strokes - 2) + strokes - 2),'*')
for x100 in range (-110, 15 , 5):
    x = x100 / 100
    r = 1.23 * x ** 5 - 2.52 * x ** 4 - 16.1 * x ** 3 + 17.3 * x ** 2
    for i in range(1, symbols + 1):
        if r < (i * interval):
            print('{:<7}|'.format(x), " " * (i-1),'*',sep='', end='')
            break
print("Значение r_min / r_max = {:1g}".format(minn / maxx))