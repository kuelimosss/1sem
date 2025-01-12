

def replace_math_expression(text,symbol_num,line_num,l,res):
    len_math = symbol_num - l - 1
    text[line_num] = text[line_num][:l]+str(res)+text[line_num][l+len_math+1:]
    

def get_calculate(operators,st,digits):
        digits.append(int(st))
        ind = 0
        # считаем сначала все деления
        while ind <(len(operators)):
            print(digits,operators)
            if operators[ind] == '/':
                if digits[ind + 1] != 0:
                    digits[ind] = digits[ind] // digits[ind + 1]
                else:
                    print('Ошибка, при вычислении выражения получилось деление на 0.')
                    print('Часть, проводящая к ошибке была автоматически заменена на 0.')
                    digits[ind] = 0
                operators.pop(ind)
                digits.pop(ind+1)
            print(digits,operators)
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
