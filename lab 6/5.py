# Лабораторная работа №6 “Списки. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 5:
# Поменять местами элементы с характеристиками по варианту
# Вариант 3:
# Минимальный положительный и максимальный положительный.

arr = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not arr:
    print('Список не может быть пустым')
    arr = list(map(int,input("Введите элементы списка через пробел: ").split()))

#Задаем максимум и минумум
#print(*arr, sep  = ', ')

id_max = -1
id_min = -1

for i in range(1, len(arr)):
    if arr[i] > 0:
        if arr[i] > arr[id_max]:
            id_max = i
        if arr[i] < arr[id_min]:
            id_min = i

if id_max == -1 or id_min == -1:
    print("В списке нет положительных элементов ")
else:
    arr[id_max],arr[id_min] = arr[id_min],arr[id_max]

    print(*arr, sep  = ', ')
    print('Были перемещены элементы, имеющие индексы {:d} и {:d}'.format(id_max,id_min))


