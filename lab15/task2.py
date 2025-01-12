import random
import struct

# Элементы, кратные трём
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


def add_doubled_values(file_name):
    with (open(file_name, "rb+") as f):
        count_3 = 0
        count_nums = 0
        while (packed_x := f.read(4)):
            x = struct.unpack("i", packed_x)[0]
            count_nums += 1
            if x % 3 == 0:
                count_3 += 1

        for _ in range(count_3):
            f.write(struct.pack("i", 0))#создаем пустые 

        if count_nums:
            f.seek(-4 * (count_3 + 1), 1)
            for _ in range(count_nums):
                packed_x = f.read(4)
                if packed_x:
                    x = struct.unpack("i", packed_x)[0]
                    if count_3:
                        if x % 3 == 0:
                            f.seek(4 * (count_3 - 2), 1)
                            f.write(packed_x)
                            f.write(struct.pack("i", x * 2))
                            f.seek(-min(f.tell(), 4 * (count_3 + 2)), 1)
                            count_3 -= 1
                        else:
                            f.seek(4 * (count_3 - 1), 1)
                            f.write(packed_x)
                            f.seek(-min(f.tell(), 4 * (count_3 + 2)), 1)

file_name = 'file.bin'
create_file(file_name)
print('Изменённый файл: ', end='')
add_doubled_values(file_name)
read_file(file_name)