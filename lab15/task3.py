import random
import struct

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


def sort(file_name):
    VALUE_SIZE = struct.calcsize("i")
    with open(file_name, "rb+") as f:
        f.seek(0, 2)
        start = 0
        end = f.tell()
        while start < end:
            curr_min = float("inf")
            curr_min_position = -1
            f.seek(start)
            while True:
                packed_x = f.read(VALUE_SIZE)
                if not packed_x:
                    break
                x = struct.unpack("i", packed_x)[0]
                if x < curr_min:
                    curr_min = x
                    curr_min_position = f.tell() - VALUE_SIZE
            packed_curr_min = packed_x = struct.pack("i", curr_min)
            f.seek(start)
            change_x = f.read(VALUE_SIZE)
            f.seek(start)
            f.write(packed_curr_min)
            f.seek(curr_min_position)
            f.write(change_x)
            start += VALUE_SIZE
file_name = 'file.bin'
create_file(file_name)
print('Изменённый файл: ', end='')
sort(file_name)
read_file(file_name)