from math import *
def func(x):
    return -x

def primitive_func(x):
    return -x**2/2

def right_rectangle_method(start,end,n):
    step = (end - start) / n 
    sum_ = 0
    for i in range(1,n):
        sum_ += func(start + (i + 1) * step)
    return (step * sum_)

def trapezoid_method(start,end,n):
    step = (end - start) / n 
    sum_ = 0
    for i in range(1,n):
        sum_ += func(start + i * step)
    return ((step / 2) * (func(start) + func(end)) + step * sum_)

def output_table(i1, i2, i3, i4, n1, n2):
    print("-" * 77)
    print(f"|{'Метод \ Количество участков ':^30}", "|", f"{n1:^19.6g}",'|', f"{n2:^19.6g}","|")
    print("-" * 77)
    print(f"|{'Метод правых прямоугольников':^30}",'|',f"{i1:^20.6g}|{i2:^20.6g}",'|')
    print("-" * 77)
    print(f"|{'Метод трапеций':^30}",'|',f"{i3:^20.6g}|{i4:^20.6g}","|")
    print("-" * 77)

def absolute_inaccuracy(x, y):
    return (abs(x - y))

def relative_inaccuracy(x, y):
    return (abs(x - y) / abs(y))

def find_better_amount_n(method, start, end, eps, max_):
    n = max_
    while abs(method(start, end, n) - method(start, end, 2 * n)) >= eps:
        n += 1
    return n
    