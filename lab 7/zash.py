arr=[]
print("Введите первый элемент списка, каждый новый элемент вводится с новой строки ")
line = input()
while line != '>>':
    arr.append(line)
    print("Введите новую строку")
    line = input()

n = 0
for i in range(len(arr)):
    if '5' not in  arr[i]:
        arr[n] = arr[i]
        n += 1

for i in range(n):
    if n - i > 1:
        print(arr[i],end =', ')
    else:
        print(arr[i],end =' ')