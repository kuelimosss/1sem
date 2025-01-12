# Лабораторная работа №6 “Списки. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 4:
# Найти наиболее длинную непрерывную последовательность по варианту
# Вариант 3:
# Возрастающая последовательность простых чисел.

arr = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not arr:
    print('Список не может быть пустым')
    arr = list(map(int,input("Введите элементы списка через пробел: ").split()))

#Обнуляем значения текущей и максимальном длины последовательности
max_len = 0
cur_len = 0
id_start = 0
for i in range(len(arr)):
    #Числа <= 1 не могут быть простыми, значит нужно обнулить текущую последовательность
    if arr[i] <= 1:
        if cur_len > max_len:
            max_len = cur_len
            id_start = i - cur_len 
        cur_len = 0
    else:

        is_simple = True
        for d in range(2, int(arr[i] ** 0.5)+1):
            if arr[i] % d == 0: #Если есть делители в заданом диапазоне, значит число не простое
                is_simple = False
                break
        if is_simple:
            #если число простое и больше предыдущего, увеличиваем длину последовательности
            if cur_len == 0 or (arr[i] > arr[i - 1] and cur_len >=1 ):
                cur_len += 1
            #если число простое, но меньше предыдущего
            else:
                if cur_len > max_len:
                    max_len = cur_len
                    id_start = i - cur_len 
                cur_len = 1
        #если число не простое 
        else:
            if cur_len > max_len:
                max_len = cur_len
                id_start = i - cur_len 
            cur_len = 0
    #если последовательность простых чисел оканчивается вметсе со всем списком, провермяем ее длину
    if i == len(arr) - 1:
        if cur_len > max_len:
            max_len = cur_len
            id_start = i - cur_len + 1
    #print(i,arr[i],cur_len,is_simple,id_start)

print('Наиболее длиная непрерывная возрастающая последовательность простых чисел =', arr[id_start : id_start + max_len])
print(id_start, max_len)
