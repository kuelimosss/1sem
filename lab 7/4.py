# Лабораторная работа №7 “Списки. Часть 2”
# Шагаев Андрей ИУ7-14Б
# Изменение элемента в списке строк по варианту.
# Вариант 1 -> Замена всех строчных согласных английских букв на заглавные
arr=[]
print("Введите первый элемент списка, каждый новый элемент вводится с новой строки ")
print("Ввод оканчивается символами '>>' ")
line = input()
while line != '>>':
    arr.append(line)
    print("Введите новую строку")
    line = input()

# в кодировке unicode буквы от a до z  имеют значение от 
# 97 до 122, а заглавные от 65 до 90, тогда разница между
# соответственными буквами = 32
for i in range(len(arr)):
    modified_elem = ''
    for symbol in arr[i]:
        if symbol not in 'eyuioa' and 97 <= ord(symbol) <= 122:
            modified_elem += chr(ord(symbol)-32)
        else:
            modified_elem += symbol
    arr[i] = modified_elem
        
print(*arr)
