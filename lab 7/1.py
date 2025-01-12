#Лабораторная работа №7 “Списки. Часть 2”
#Шагаев Андрей ИУ7-14Б
#Удалить все элементы целочисленного списка, имеющие свойство 
#по варианту, за один цикл. Без del pop remove срезов
#Вариант 3 -> Нечётные элементы
arr = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not arr:
    print('Список не может быть пустым')
    arr = list(map(int,input("Введите элементы списка через пробел: ").split()))


n = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[n] = arr[i]
        n += 1

for i in range(n):
    if n - i > 1:
        print(arr[i],end =', ')
    else:
        print(arr[i],end =' ')
