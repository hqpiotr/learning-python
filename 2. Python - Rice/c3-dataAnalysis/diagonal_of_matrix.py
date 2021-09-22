import random


def compute_diagonal(matrix):
    result = 0
    print("\n\n")
    for i in range(len(matrix)):
        # print(matrix[i][i])
        result += int(matrix[i][i])
    return result

def fill_in_square_matrix(n):
    matrix = []
    for row in range(n):
        values = []
        for col in range(n):
            values.append(row * col)
        matrix.append(values)
    return matrix

"""
[ 1 2 3 ]
[ 4 5 6 ]
[ 7 8 9 ]
"""
m = []
m = fill_in_square_matrix(5)
for i in m:
    print(i)
print("result =", compute_diagonal(m))

auto_list = [[i + 4*j for i in range(1, 5)] for j in range(1, 5)]
for x in auto_list:
    print(x)
