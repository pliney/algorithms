import random
from pprint import pprint as pp


matrix = []
rows = 9
columns = 3

def gen_array():
    assert(rows % columns == 0)
    column_list = []
    for i in range(0, columns):
        column = []
        for j in range(0, rows):
            column.append(random.randint(0,1000))
        column_list.append(column)
    return column_list

def sort_columns():
    for i in range(0, len(matrix)):
        matrix[i].sort()

def gen_temp(r, c):
    temp = []
    for i in range(0, c):
        column = [None]*r
        temp.append(column)
    return temp

def transpose():
    temp = gen_temp(len(matrix[0]), len(matrix))
    count = 0
    for i in range (0, rows):

        for j in range(0, columns):
            temp[j][i] = matrix[count / rows][count % rows]
            count += 1
    return temp

def untranspose():
    temp = gen_temp(len(matrix[0]), len(matrix))
    count = 0
    for i in range (0, rows):

        for j in range(0, columns):
            temp[count / rows][count % rows] = matrix[j][i]
            count += 1
    return temp

def slide():
    temp = gen_temp(len(matrix[0]), len(matrix) + 1)
    for i in range(0, len(temp[0])):
        temp[len(temp)-1][i] = float('inf')
    first = True
    count = 0
    for i in range(0, len(temp)):
        if first:
            j = len(temp[0])/2
            first = False
        else:
            j = 0
        while j < len(temp[0]) and count < rows * columns:
            temp[i][j] = matrix[count / rows][count % rows]
            count += 1
            j += 1
    return temp

def unslide():
    temp = gen_temp(len(matrix[0]), len(matrix))
    first = True
    count = 0
    for i in range(0, len(temp)):
        if first:
            j = len(temp[0])/2
            first = False
        else:
            j = 0
        while j < len(temp[0]) and count < rows * columns:
            temp[count / rows][count % rows] = matrix[i][j]
            count += 1
            j += 1
    del temp[len(temp) - 1]
    return temp


def print_array(a):
    pp(zip(*a))

def test_c_sort():
    print_array(matrix)
    sort_columns()
    print_array(matrix)

def test_transpose():
    print_array(matrix)
    print_array(transpose())

def test_untranspose():
    print_array(matrix)
    print_array(untranspose())

def test_slide():
    print_array(matrix)
    m = slide()
    print_array(m)
    return m


def test_unslide():
    print_array(matrix)
    m = unslide()
    print_array(m)
    return m

def test_functions():
    global matrix
    matrix = gen_array()
    print_array(matrix)
    print('c sort:')
    test_c_sort()
    print('transpose:')
    test_transpose()
    print('untranpose:')
    test_untranspose()
    print('slide:')
    matrix = test_slide()
    matrix = test_unslide()

def group_sort():
    global matrix
    matrix = gen_array()

    sort_columns()
    matrix = transpose()
    sort_columns()
    matrix = untranspose()
    sort_columns()
    matrix = slide()
    sort_columns()
    matrix = unslide()

    print_array(matrix)

if __name__ == '__main__':
    rows = 36
    columns = 6
    # test_functions()
    group_sort()


