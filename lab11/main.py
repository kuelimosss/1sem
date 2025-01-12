from my_functions import *
from random import * 

user_array = array_input()

selected_sort = simple_select_sort

print("Сортировка массива, заданного пользователем: \n",*selected_sort(user_array, True))

n1, n2, n3 = num_input(1), num_input(2), num_input(3) 

random_array_n1 = [randint(-1000,1000) for x in range(n1)]
random_array_n2 = [randint(-1000,1000) for x in range(n2)]
random_array_n3 = [randint(-1000,1000) for x in range(n3)]

sorted_array_n1 = sorted(random_array_n1)
sorted_array_n2 = sorted(random_array_n2)
sorted_array_n3 = sorted(random_array_n3)

reverse_sorted_array_n1 = sorted(random_array_n1,reverse=True)
reverse_sorted_array_n2 = sorted(random_array_n2,reverse=True)
reverse_sorted_array_n3 = sorted(random_array_n3,reverse=True)


t1,k1 = selected_sort(sorted_array_n1, False)
t2,k2 = selected_sort(sorted_array_n2, False)
t3,k3 = selected_sort(sorted_array_n3, False)

t4,k4 = selected_sort(random_array_n1, False)
t5,k5 = selected_sort(random_array_n2, False)
t6,k6 = selected_sort(random_array_n3, False)

t7,k7 = selected_sort(reverse_sorted_array_n1, False)
t8,k8 = selected_sort(reverse_sorted_array_n2, False)
t9,k9 = selected_sort(reverse_sorted_array_n3, False)
# придумать как использовать получееное в функции количество перестановок 
# 

print("-" * 108)
print("|"," " * 20,"|",f"{n1:^25.7g}","|",f"{n2:^25.7g}","|",f"{n3:^25.7g}","|")
print("-" * 108)
print("|"," " * 20,"|",f"{'Время':^10}","|",f"{'Перестановки':^12}","|",f"{'Время':^10}","|",f"{'Перестановки':^12}","|",f"{'Время':^10}","|",f"{'Перестановки':^12}","|")
print("-" * 108)
print("|",f"{'Упорядеченный список':^20}","|",f"{t1:^10.8f}","|",f"{k1:^12}","|",f"{t2:^10.8f}","|",f"{k2:^12}","|",f"{t3:^10.8f}","|",f"{k3:^12}","|")
print("-" * 108)
print("|",f"{'Рандомный список':^20}","|",f"{t4:^10.8f}","|",f"{k4:^12}","|",f"{t5:^10.8f}","|",f"{k5:^12}","|",f"{t6:^10.8f}","|",f"{k6:^12}","|")
print("-" * 108)
print("|",f"{'Обратно упор. список':^20}","|",f"{t7:^10.8f}","|",f"{k7:^12}","|",f"{t8:^10.8f}","|",f"{k8:^12}","|",f"{t9:^10.8f}","|",f"{k9:^12}","|")
print("-" * 108)