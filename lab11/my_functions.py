import time

def simple_select_sort(array, first_time):
    start = time.time()
    k = 0
    for i in range(len(array) -1):
        min_index = i
        for j in range(i,len(array)):
            if array[j] <  array[min_index]:
                min_index = j
        if min_index != i:
               array[min_index], array[i] = array[i], array[min_index]
               k += 1
    finish = time.time()
    work_time = finish - start
    if first_time:
        return array
    else:
        return work_time, k
    

def array_input(): 
    while True:
        try:
            a = list(map(int,input("Введите целочисленный массив: ").split()))
        except ValueError:
            print("В списке могут находиться только целые числа")
        else:
            break
     
    return a
        

def num_input(count): 
    while True:
        try:
            n = int(input(f"Введите размер массива № {count}: "))
        except ValueError:
            print("Убедитесь, что вводите число")
        else:
            break
    
    return n

