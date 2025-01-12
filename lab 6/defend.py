arr=list(map(int,input("vvod").split()))
for i in range(len(arr)):
    num = arr[i]
    reverse = s = 0
    while num > 0:
        reverse += num % 10
        s += num % 10
        num //= 10
        reverse *= 10
    reverse //= 10
    if reverse == arr[i]:
        arr[i] = s
print(*arr)