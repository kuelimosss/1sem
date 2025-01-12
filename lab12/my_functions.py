def print_menu():
    print("""Функциональное меню: 
    0. Выход из программы.
    1. Выровнять текст по левому краю.
    2. Выровнять текст по правому краю.
    3. Выровнять текст по ширине.
    4. Удаление всех вхождений заданного слова.
    5. Замена одного слова другим во всём тексте.
    6. Вычитание и деление целых чисел внутри текста.
    7. Найти (вывести на экран) и затем удалить предложение с максимальным количеством слов,
       начинающихся на заданную букву.
          """)
    

def print_text(text):
    print(*text,'\n',sep='\n')


def get_max_line(text): 
    max_len = -1
    for i in range(len(text)):
        max_len = max(max_len,len(text[i]))
    return max_len


def left_align(text): # 1 point
    for line_num in range(len(text)):
        text[line_num] = ' '.join(text[line_num].split()) # убираем все лишние пробелы между строк
        #text[line_num] = text[line_num].lstrip()
    return text


def right_align(text): # 2 point
    max_width = get_max_line(text)
    for line_num in range(len(text)):
        text[line_num] = ' '.join(text[line_num].split()) # убираем все лишние пробелы между строк
        cur_width = len(text[line_num])
        count_space = (max_width - cur_width) * ' ' 
        text[line_num] = count_space + text[line_num]
    return text


def width_align(text): # 3 point
    max_width = get_max_line(text)
    for line_num in range(len(text)):
        text[line_num] = ' '.join(text[line_num].split()) # убираем все лишние пробелы между строк
        cur_width = len(text[line_num]) # длина текущей строки 
        if cur_width != max_width:
            words = text[line_num].split()
            if max_width - cur_width >= len(words) - 1 and (len(words) - 1 != 0): # правая часть неравентса - одинарные пробелы между словами
                need_space = (max_width - cur_width)// (len(words) - 1) + 1
            else:
                need_space = 1
            if len(words) - 1 != 0:
                extra_space = (max_width - cur_width) % (len(words) - 1)
            else:
                extra_space = 0
            for i in range(1,len(words)):
                if i <= extra_space:
                    space = ' ' * (need_space +1)
                    words[i] = space + words[i]
                else:
                    space = ' ' * need_space
                    words[i] = space + words[i]
            text[line_num] = ''.join(words)
    return text


#слова могут находится в начале и в конце строк, где нет ни точки ни запятой ни пробела скраю
def remove_user_word(text,word): # 4 point
    for line_num in range(len(text)):
        words = text[line_num].split()
        for i in range(len(words)):
            if '.' in words[i] or ',' in words[i]:
                if word == words[i][:-1]:
                    text[line_num] = text[line_num].replace(f' {word}',',')
            else:
                if word == words[i]:
                    text[line_num] = text[line_num].replace(f' {word}','').replace(f'{word} ','')
    return text


def replace_user_word(text,word,new_word): # 5 point
    for line_num in range(len(text)):
        words = text[line_num].split()
        for i in range(len(words)):
            if '.' in words[i] or ',' in words[i]:
                if word == words[i][:-1]:
                    text[line_num] = text[line_num].replace(f' {word}',f' {new_word}')
            else:
                if word == words[i]:
                    text[line_num] = text[line_num].replace(f' {word}','').replace(f'{word} ',f' {new_word}')
    return text


def replace_math_expression(text,symbol_num,line_num,l,res): # подфунция для 6 point
    len_math = symbol_num - l - 1
    text[line_num] = text[line_num][:l]+str(res)+text[line_num][l+len_math+1:]
    

def get_calculate(operators,st,digits): # подфунция для 6 point
        digits.append(int(st))
        ind = 0
        # считаем сначала все деления
        while ind <(len(operators)):
            if operators[ind] == '/':
                if digits[ind + 1] != 0:
                    digits[ind] = digits[ind] // digits[ind + 1]
                else:
                    print('Ошибка, при вычислении выражения получилось деление на 0.')
                    print('Часть, проводящая к ошибке была автоматически заменена на 0.')
                    digits[ind] = 0
                operators.pop(ind)
                digits.pop(ind+1)
            ind += 1
            # теперь среди наших выражений остались только вычитания, можем вычитать числа одно за другим, начиная с первого
            res = digits[0]
            for num_ind in range(len(digits)-1):
                res -= digits[num_ind + 1]
        return res

def calc_arithmetic(text): # 6 point
    numbers = '0123456789'
    l = -1
    for line_num in range(len(text)):
        symbol_num = 0
        digits = []
        operators = []
        st = ''
        while symbol_num < len(text[line_num]):
            symbol = str(text[line_num][symbol_num])
            
            # если элемент - пробел, то просто пропускаем его
            while symbol == ' ':
                symbol_num += 1
                symbol = str(text[line_num][symbol_num])
            # запоминаем номер первого появления цифры( вокруг него завязаны: замена подстроки с выражением, определение начала и конца каждого числа, вычисление и др.)   
            if symbol in numbers:
                st += symbol
                if l == -1:
                    #remember_line = line_num
                    l = symbol_num

            # после получения числа, берем первый знак (что первое попалось после числа - то и выполняем)
            elif symbol in '-/':
                if len(st)!= 0:
                    digits.append(int(st))
                    operators.append(symbol)
                    st = ''

            elif l!= -1:
                if len(operators)!= 0 and len(st) != 0:
                    res = get_calculate(operators,st,digits)
                    replace_math_expression(text,symbol_num,line_num,l,res)
                l = -1
                st = ''
                digits=[]
                operators=[]
            symbol_num += 1  
        if len(operators)!= 0 and len(st) != 0:
                    res = get_calculate(operators,st,digits)
                    replace_math_expression(text,symbol_num,line_num,l,res)  
    return text


def find_user_sent(text): # 7 point
    max_count = 0
    cur_max_len = 0
    max_sentence_start = (0, 0)
    max_sentence_end = (0, 0)
    sentence_start = (0, 0)
    word = ''
    for line_ind in range(len(text)):
        for symbol_ind in range(len(text[line_ind])):
            symbol = text[line_ind][symbol_ind]
            if symbol.isalpha():
                word += symbol
            else:
                if word:
                    if len(word) > cur_max_len:
                        cur_max_len = len(word) 
                word = ''
            if symbol in '!.?' or (line_ind == len(text) - 1 and symbol_ind == len(text[line_ind]) - 1):
                sentence_end = (line_ind, symbol_ind)
                if max_count < cur_max_len:
                    max_count = cur_max_len
                    max_sentence_start = sentence_start
                    max_sentence_end = sentence_end
                cur_max_len = 0
                if symbol in '!.?':
                    sentence_start = (line_ind, symbol_ind + 1)

    answer = ''

    if max_sentence_end != (0, 0):
        rows_to_delete = []
        if max_sentence_start[0] != max_sentence_end[0]:
            answer += text[max_sentence_start[0]][max_sentence_start[1]:]
            text[max_sentence_start[0]] = (text[max_sentence_start[0]][:max_sentence_start[1]]).strip()

            for row_ind in range(max_sentence_start[0] + 1, max_sentence_end[0]):
                answer += text[row_ind]
                rows_to_delete.append(row_ind)

            answer += ' ' +text[max_sentence_end[0]][:max_sentence_end[1] + 1]
            text[max_sentence_end[0]] = (text[max_sentence_end[0]][max_sentence_end[1] + 1:]).strip()
        else:
            answer += ' ' + text[max_sentence_start[0]][max_sentence_start[1]:max_sentence_end[1] + 1]
            text[max_sentence_start[0]] = ((text[max_sentence_start[0]][:max_sentence_start[1]] + ' ' + text[max_sentence_start[0]][max_sentence_end[1] + 1:])).strip()

        for row_ind in rows_to_delete[::-1]:
            del text[row_ind]
    else:
        answer = 'Таких предложений нет.'

    print(f'Результат: {answer}','\n')

    return text


def processing_user_choice(text,point):
    match point:
        case 1:
            text = left_align(text)
            print_text(text)
            print_menu()
        case 2:
            text = right_align(text)
            print_text(text)
            print_menu()
        case 3:
            text = width_align(text)
            print_text(text)
            print_menu()
        case 4:
            word  = input("Введите слово, каждое из вхождений которого вы хотите удалить: \n")
            text = remove_user_word(text,word)
            print_text(text)
            print_menu()
        case 5:
            word  = input("Введите слово, каждое из вхождений которого вы хотите заменить: \n")
            new_word = input("Введите слово, НА КОТОРОЕ будет произведена замена: \n")
            text = replace_user_word(text,word,new_word)
            print_text(text)
            print_menu()
        case 6:
            text = calc_arithmetic(text)
            print_text(text)
            print_menu()
        case 7:
            #letter =  input("Введите букву, для выполнения условия пункта: \n")
            text = find_user_sent(text)
            print_text(text)
            print_menu()
        

def get_user_choice():
    while True:
        try:
            point = int(input("Введите номер действия (1-7), чтобы выполнить его:\n"))
        except ValueError:
            print("Убедитесь, что вводите целое число")
        else:
            if point < 0  or point > 7:
                print('Убедитесь, что вводите целое число от 1 до 7:')
            else:
                break
    return point
    


def second_width_align(text): # 3 point
    max_width = get_max_line(text)
    for i in range(len(text)):
        words = text[i].split()
        text[i] = ' '.join(text[i].split()) # убираем все лишние пробелы между строк
        cur_width = len(text[i]) # длина текущей строки 
        total_spaces = max_width - cur_width # всего осталось добавить пробелов
        #more_spaces = total_spaces % count_words
        text[i] = ' '.join(words)
        if total_spaces != 0:
            flag = True
            while flag:
                for ind in range(len(words)-1):
                    print(text[i],'|||',total_spaces,'\n')
                    text[i] = text[i].replace(f'{words[ind]}',f'{words[ind]} ',1)
                    total_spaces -= 1
                    if total_spaces == 0:
                        flag = False
                        break
    print_text(text)
    get_user_choice(text)