'''
Шагаев Андрей ИУ7-14Б
Лабораторная работа №13 “База данных в текстовом файле”
Требуется написать программу, которая позволит с помощью меню выполнить
следующие действия:
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в конец базы данных
5. Поиск по одному полю
6. Поиск по двум полям
'''
from my_functions import print_menu, get_user_choice, processing_user_choice
import os

def main():
    file_path = None
    print("БАЗА ДАННЫХ СОДЕРЖИТ СЛЕДУЮЩИЕ ПОЛЯ:")
    print("Имя, Фамилия, № Зачетки, Номер телеофна")
    print_menu()
    point = get_user_choice()
    while point != 0:
        if point == 1:
            file_path = input("Введите абсолютный путь к файлу: \n")
            while not os.path.exists(file_path) or file_path[-4:]!='.txt':
                print("Введен некорректный путь, введите еще раз.")
                file_path = input("Введите абсолютный путь к файлу: \n")
        processing_user_choice(point,file_path)
        point = get_user_choice()

if __name__ ==  '__main__':
    main()