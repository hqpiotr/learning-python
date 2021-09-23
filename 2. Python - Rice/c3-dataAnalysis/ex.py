NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict

# print(my_matrix)
d_frmt = '{:<4} {:<4}'
for k,v in my_matrix.items():
    print("{", k, "}", "\t", v)

frmt = '{:<4}'
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(frmt.format(my_matrix[row][col]), end='')
    print()