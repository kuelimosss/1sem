file_path = '123.txt'
with open(file_path, 'w') as file:
    print("Введите новую запись базы данных, разделитель -  ','.\nЧтобы закончить ввод, введите 'exit'")
    print("Запись должна содержать 4 поля, последнее из которых - числовое\n")
    while True:
        record = input("Введите новую запись базы данных, разделитель -  ','.\nЧтобы закончить ввод, введите 'exit': \n")
        if record == 'exit':
            break
        fields = record.split(',')
        if len(fields) != 4:
            print("\nЗапись должна содержать 4 поля, последнее из которых - числовое\n")
            continue
        if not fields[3].strip().isdigit():
            print("\nЧетвёртое поле записи должно быть числовым\n")
            continue
        file.write(record + '\n')



