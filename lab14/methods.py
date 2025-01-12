import os
import struct

struct_format = "20s10sq"
pack_size = struct.calcsize(struct_format)

def print_menu():
    print('Доступные операции с базой данных:')
    print('0. Завершить работу программы')
    print('1. Выбрать файл для работы')
    print('2. Инициализировать базу данных')
    print('3. Вывести содержимое базы данных')
    print('4. Добавить запись в произвольное место базы данных')
    print('5. Удалить произвольную запись из базы данных')
    print('6. Поиск по одному полю')
    print('7. Поиск по двум полям')
    print()

def pack_to_bin(lastname: str, document: str, phone_number: int) -> bytes:
    lastname = lastname.encode("utf-8")
    document = document.encode("utf-8")
    packed_data = struct.pack(struct_format, lastname, document, phone_number)
    return packed_data

def db_initialization(file_name: str) -> str:
    if not file_name:
        file_name = "db"
    data = open(f"{file_name}.bin", "wb+")
    data.close()
    return file_name

def db_print(file_path: str):
    with open(file_path, 'rb') as file:
        print("Фамилия             Зачётка             Номер телефона")
        while packed_line := file.read(pack_size):
            lastname, document, phone_number = struct.unpack(struct_format, packed_line)
            lastname, document = lastname.decode("utf-8").rstrip("\x00"), document.decode("utf-8").rstrip("\x00")
            print(lastname.ljust(20, ' ') + document.ljust(20, ' ') + str(phone_number))

def add_record(file_path: str, lastname: str, document: str, phone_number: int, position: int):
    with open(file_path, "rb+") as file:
        file.seek(pack_size * (position - 1))
        insertion = pack_to_bin(lastname, document, phone_number)
        while line := file.read(pack_size):
            file.seek(-pack_size, 1)
            file.write(insertion)
            insertion = line
        file.write(insertion)

def remove_record(file_path: str, position: int):
    with open(file_path, "rb+") as file:
        file.seek(pack_size * (position - 1))
        while file.read(pack_size) and (next_line := file.read(pack_size)):
            file.seek(-2 * pack_size,1)
            file.write(next_line)
        file.seek(-pack_size, 2)
        file.truncate()

def search_by_one(file_path: str, search_by):
    if search_by == "Фамилия":
        necessary = input("Введите первые буквы фамилии: ")
        with open(file_path, 'rb') as file:
            print("Фамилия             Зачётка             Номер телефона")
            while packed_line := file.read(pack_size):
                lastname, document, phone_number = struct.unpack(struct_format, packed_line)
                lastname, document = lastname.decode("utf-8").rstrip("\x00"), document.decode("utf-8").rstrip("\x00")
                if lastname[:len(necessary)] == necessary:
                    print(lastname.ljust(20, ' ') + document.ljust(20, ' ') + str(phone_number))

    else:
        necessary = input("Введите последние цифры номера телефона: ")
        with open(file_path, 'rb') as file:
            print("Фамилия             Зачётка             Номер телефона")
            while packed_line := file.read(pack_size):
                lastname, document, phone_number = struct.unpack(struct_format, packed_line)
                lastname, document, phone_number = lastname.decode("utf-8").rstrip("\x00"), document.decode("utf-8").rstrip("\x00"), str(phone_number)
                if necessary == phone_number[-len(necessary):]:
                    print(lastname.ljust(20, ' ') + document.ljust(20, ' ') + str(phone_number))

def search_by_two(file_path):
    print("Поиск осуществляется по полям Фамилия и Номер телефона.")
    necessary_lastname = input("Введите первые буквы фамилии: ")
    necessary_phonenumber = input("Введите последние цифры номера телефона: ")
    with open(file_path, 'rb') as file:
        while packed_line := file.read(pack_size):
            lastname, document, phone_number = struct.unpack(struct_format, packed_line)
            lastname, document, phone_number = lastname.decode("utf-8").rstrip("\x00"), document.decode("utf-8").rstrip("\x00"), str(phone_number)
            if necessary_phonenumber == phone_number[-len(necessary_phonenumber):] and lastname[:len(necessary_lastname)] == necessary_lastname:
                print(lastname.ljust(20, ' ') + document.ljust(20, ' ') + str(phone_number))

def get_user_num(welcoming, start=float("-inf"), end=float("inf")):
    while True:
        try:
            element = int(input(welcoming))
            if start <= element <= end:
                return element
            else:
                print(f'Это не целое число от {start} до {end}, повторите ввод')
        except:
            print('Это не целое число, повторите ввод')



