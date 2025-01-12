#Лабораторная работа №7 “Списки. Часть 2”
#Шагаев Андрей ИУ7-14Б
#Поиск элемента в списке строк по варианту.
#Вариант 7 -> Поиск наиболее короткого элемента, не содержащего пробелов
arr=[]
print("Введите первый элемент списка, каждый новый элемент вводится с новой строки ")
print("Ввод оканчивается символами '>>' ")
line = input()
while line != '>>':
    arr.append(line)
    print("Введите новую строку")
    line = input()
len_min = float('+inf')
el_min = ' '
is_anyone_here = False
for elem in arr:

    if elem.count(" ") == 0:
        is_anyone_here = True
        if len(elem) < len_min:
            len_min = len(elem)
            el_min = elem
if is_anyone_here:
    print("Самый короткий элемент, не содержащий пробелов:",el_min)
else:
    print("Во всём списке не нашлось ни одного элемента без пробелов")
