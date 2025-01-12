def print_menu():
    print("""Функциональное меню: 
    1. Выбрать файл для работы
    2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
    его записями)
    3. Вывести содержимое базы данных
    4. Добавить запись в конец базы данных
    5. Поиск по одному полю
    6. Поиск по двум полям
          """)


def create_base(file_path):
    print("\nЕсли вы выбрали какой-либо файл, то он будет полностью перезаписан.")
    ans = input("Вы хотите продолжить? (д/н)")
    if ans.lower() == 'д': 
        with open(file_path, 'w') as file:
            print("\nВведите новую запись базы данных, разделитель -  ','.\nЧтобы закончить ввод, введите 'exit'")
            print("Запись должна содержать 4 поля.\n")

            while (record := input("Введите новую запись\n")) != 'exit':
                good_record = True
                fields = record.split(',')
                if len(fields) != 4:
                    print("\nЗапись должна содержать 4 поля, последнее из которых - числовое\n")
                    good_record = False
                elif not fields[3].strip().isdigit():
                    print("\nЧетвёртое поле записи должно быть числовым\n")
                    good_record = False
                if good_record:
                    file.write(record)
                else:
                    good_record = True


def base_output(file_path):   
    print("\nИмя, Фамилия, № Зачетки, Номер телеофна")
    with open(file_path, 'r') as file:
        for record in file:
            print(record)


def append_record(file_path):
    with open(file_path, 'a') as file:
            print("\nВведите новую запись базы данных, разделитель -  ','.\nЧтобы закончить ввод, введите 'exit'")
            print("Запись должна содержать 4 поля, последнее из которых - числовое\n")

            while (record := input("Введите новую запись\n")) != 'exit':
                good_record = True
                fields = record.split(',')
                if len(fields) != 4:
                    print("\nЗапись должна содержать 4 поля, последнее из которых - числовое\n")
                    good_record = False
                elif not fields[3].strip().isdigit():
                    print("\nЧетвёртое поле записи должно быть числовым\n")
                    good_record = False
                if good_record:
                    file.write(record )
                else:
                    good_record = True


def find_with_one(file_path,field_to_find,searched_field):
    is_found = False
    with open(file_path, 'r') as file:
        for record in file:
            record1 = record.replace(', ',',')
            fields = record1.split(",")
            if fields[field_to_find].lower() == searched_field.lower():
                is_found = True
                print("Найдено:", record)
    if not is_found:
        print("Не было найдени ни одной записи")
            

def find_with_two(file_path,field_to_find1,field_to_find2,searched_field1,searched_field2):
    is_found = False
    with open(file_path, 'r') as file:
        for record in file:
            record1 = record.replace(', ',',')
            fields = record1.split(",")
            if (fields[field_to_find1].lower() == searched_field1.lower()) and (fields[field_to_find2].lower() == searched_field2.lower()):
                is_found = True
                print("Найдено:", record)
    if not is_found:
        print("Не было найдени ни одной записи")

def processing_user_choice(point,file_path):
    match point:
        case 2:
            if file_path:
                print("Выбранный файл: ", file_path)
                create_base(file_path)
                print_menu()
            else:
                print('Вы не выбрали файл, поэтому будет создан новый файл в этой директории.\n')
                file_name = input("Введите название нового файла: ")
                create_base(file_name)
                print_menu()
        case 3:
            if file_path:
                print("Выбранный файл: ", file_path)
                base_output(file_path)
                print_menu()
            else:
                print("Сначала Вам нужно выбрать файл")
        case 4:
            if file_path:
                print("Выбранный файл: ", file_path)
                append_record(file_path)
                print_menu()
            else:
                print("Сначала Вам нужно выбрать файл")
        case 5:
            if file_path:
                print("Выбранный файл: ", file_path)
                print("\nСуществующие поля для поиска\n")
                print(*("Имя - 1","Фамилия - 2","№ Зачетки - 3","Номер телефона - 4"))
                while (field_to_find :=  str(input("Выберите поле для поиска (Введите номер столбца): ")))  not in ("1","2","3","4"):# в каком столбце искать
                    print("Выберите поле из существующих.")
                searched_field = input("Введите значение для поиска: ") # искомое поле
                find_with_one(file_path,(int(field_to_find)-1),searched_field)
                print_menu()
            else:
                print("Сначала Вам нужно выбрать файл")
        case 6:
            if file_path:
                print("Выбранный файл: ", file_path)
                print(*("Имя - 1","Фамилия - 2","№ Зачетки - 3","Номер телефона - 4"))
                field_to_find1 = str(input("Выберите поле для поиска №1 (Введите номер столбца): "))
                while field_to_find1 not in ("1","2","3","4"):# в каком столбце искать
                    print("Выберите поле из существующих.")
                    field_to_find1 = str(input("Выберите поле для поиска №1 (Введите номер столбца): "))
                searched_field1 = input("Введите значение для поиска №1: ") # искомое поле
                print("\nСуществующие поля для поиска\n")
                print(*("Имя - 1","Фамилия - 2","№ Зачетки - 3","Номер телефона - 4"))
                while (field_to_find2 := str(input("Выберите поле для поиска №2 (Введите номер столбца): "))) == field_to_find1 or (field_to_find2 not in ("1","2","3","4")): # в каком столбце искать
                    print("Выберите поле из существующих. Поля не должны совпадать")
                searched_field2 = input("Введите значение для поиска №2: ") # искомое поле
                find_with_two(file_path,(int(field_to_find1)-1),(int(field_to_find2)-1),searched_field1,searched_field2)
                print_menu()
            else:
                print("Сначала Вам нужно выбрать файл")


def get_user_choice():
    while True:
        try:
            point = int(input("Введите номер действия (0-6), чтобы выполнить его:\n"))
        except ValueError:
            print("Убедитесь, что вводите целое число")
        else:
            if point < 0  or point > 7:
                print('Убедитесь, что вводите целое число от 0 до 6:')
            else:
                break
    return point