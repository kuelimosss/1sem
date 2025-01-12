"""
Шагаев Андрей ИУ7-14Б
Лабораторная работа №14 База данных в бинарном файле.
Требуется написать программу, которая позволит с помощью меню выполнить
следующие действия:
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных (пользователь указывает
номер позиции, в которую должна быть вставлена запись)
5. Удалить произвольную запись из базы данных (пользователь указывает номер
удаляемой записи)
6. Поиск по одному полю
7. Поиск по двум полям
 """
import os.path
from methods import db_initialization, db_print, add_record, remove_record, search_by_one, search_by_two, get_user_num, print_menu

def main():
    file_path=""
    print_menu()
    operation = get_user_num('Введите номер операции: ', 0, 7)
    while operation != 0:
        match operation:
            case 1:
                while not (os.path.isfile((file_path := input('Введите имя бинарного файла, хранящего базу данных: '))) and file_path[-4:] == ".bin"):
                    print("Некорректное имя файла, попробуйте снова.")
            case 2:
                db_initialization(input('Введите название базы данных: '))
            case 3:
                if file_path:
                    db_print(file_path)
                else:
                    print("Файл для работы не выбран.")
            case 4:
                if file_path:
                    lastname = input("Введите Фамилию: ")
                    document = input("Введите номер зачётки: ")
                    phone_number = get_user_num("Введите номер телефона: ", 80000000000, 89999999999)
                    position = get_user_num("Введите индекс строки, куда хотите вставить данные: ", 0)
                    add_record(file_path, lastname[:10], document[:8], phone_number, position) #в формате записи указано 20s - ограничение 10 символов на русской раскладке
                else:
                    print("Файл для работы не выбран.")
            case 5:
                if file_path:
                    position = get_user_num("Введите индекс строки, которую хотите удалить: ", 0)
                    remove_record(file_path, position)
                else:
                    print("Файл для работы не выбран.")
            case 6:
                if file_path:
                    while (search_by := input("Введите поле, по которому хотите искать (Фамилия или Телефон): ")) not in {"Фамилия", "Телефон"}:
                        print("Некорректный ввод, попробуйте снова.")
                    search_by_one(file_path, search_by)
                else:
                    print("Файл для работы не выбран.")
            case 7:
                if file_path:
                    search_by_two(file_path)
                else:
                    print("Файл для работы не выбран.")
        print_menu()
        operation = get_user_num('Введите номер операции: ', 0, 7)
if __name__ == '__main__':
    main()