text = [
    '20-10/2Место для поединка было выбрано шагах в восьмидесяти от дороги, на которой3/3',
    'остались сани, на  полянке сосновог6о леса, покрытой истаявшим',
    '10-5*4-2'
    'от стоявших последние дни оттепелей снегом. Минуты три все к к к к к к к. Противники сорока',
    'друг от 3 друга, у краев поляны. Секунданты,7 размеря8я шаги, проложили отпечатавшиеся по',
    'мокрому глубокому снегу следы от того места, где они стояли, до сабель',
    'Несвицкого и Денисова, означавших барьер и воткнутых в десяти шагах',
    'д33-3/3руг от друга. Оттепель за сорок шаго7в неясно было'
]

def print_text(text):
    print('\n',*text,'\n',sep='\n')


def get_max_line(text): 
    max_len = -1
    for i in range(len(text)):
        max_len = max(max_len,len(text[i]))
    return max_len

def find_user_sent(text): # 7 point
    sent = ''
    sentences = []
    sent_num_to_delete = -1
    # добавляем один лишний спец. символ, чтобы потом по нему определить, где были строки
    for line_num in range(len(text)):
        text[line_num] = text[line_num] + '*'
    for line_num in range(len(text)):
        for symbol_num in range(len(text[line_num])):
            #формируем список из предложений
            symbol = text[line_num][symbol_num]
            if symbol != '.' and symbol != '!' and symbol != '?':
                sent += symbol
            else:
                sentences.append(sent+'.')
                sent = ''
    # запрашиваем букву и сравниваем с первой буквой каждого слов в предложении
    letter =  input("Введите букву, для выполнения условия пункта: \n")
    max_match = 0
    for sent_num in range(len(sentences)):
        current_match = 0
        words = sentences[sent_num].split()
        for word in words:
            if letter.upper() == word.capitalize()[0]:
                current_match += 1
        if current_match > max_match:
            max_match = current_match
            sent_num_to_delete = sent_num
    # есл ничего не  нашлось, убираем спец. символ и возвращаем исходный текст
    if sent_num_to_delete != -1:
        sentences.pop(sent_num_to_delete)
    else:
        for line in range(len(text)):
            text[line] = text[line][:-1]
        print('Ни в одном из предложений не нашлось ни одного слова, начинающегося с заданной буквы\n')
        return text
    # перестраиваем текст по добавленным ранее сппец. символам 
    rebuilded_text =[]
    line = ''

    for sent_num in range(len(sentences)):
        for symbol_num in range(len(sentences[sent_num])-1):
            symbol = sentences[sent_num][symbol_num]

            if symbol!= '*':
                line += symbol
            else:
                rebuilded_text.append(line)
                line = ''
    rebuilded_text.append(line)
    return rebuilded_text


find_user_sent(text)
print('fin')
