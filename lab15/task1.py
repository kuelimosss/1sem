'''
Шагаев Андрей ИУ7-14Б
Лабораторная работа №15 “Бинарные файлы”
Чётные элементы
'''
import struct
import random


def read_file(file_name):
    with open(file_name, 'rb') as file:
        while el := file.read(4):
            print(struct.unpack('i', el)[0], end=' ')


def create_file(file_name):
    arr = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]
    print('Изначальная последовательность: ', end='')
    for el in arr:
        print(el, end=' ')
    print('\n')
    with open(file_name, 'wb') as file:
        for el in arr:
            file.write(struct.pack('i', el))


# удаление положительных
def remove_even(file_name):
    with open(file_name, "rb+") as f:
        count_even = 0
        while packed_x := f.read(4):
            x = struct.unpack("i", packed_x)[0]
            if x % 2 == 0:
                count_even += 1
            elif count_even > 0 and x % 2 == 1:
                f.seek(-4 * (count_even + 1), 1)
                f.write(packed_x)  # write передвигает указатель на 4 байта
                f.seek(4 * count_even,1)
        f.seek(-4 * count_even,1)
        f.truncate()

file_name = 'file.bin'
create_file(file_name)
print('Изменённый файл: ', end='')
remove_even(file_name)
read_file(file_name)