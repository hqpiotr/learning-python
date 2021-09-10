# input/regex_sum_1353131.txt --> There are 90 values with a sum=445833
# input/regex_sum_42.txt --> There are 69 values and the sum ends with 973
import re

def solution_2_calc_numbers_from_file(filename):
    try:
        file = open(filename)
    except:
        print('file error')
        quit()

    ints = []
    for line in file:
        strings_list = re.findall('[\d]+', line)

        for word in strings_list:
            ints.append(int(word))
    print('#' + str(len(int_values)) + ': ' + str(sum(int_values)))


def solution_1_calc_numbers_from_file(filename):
    try:
        file = open(filename)
    except:
        print('file error')
        quit()

    values = re.findall('[\d]+', file.read())

    ints = []
    for v in values:
        ints.append(int(v))
    print("#" + str(len(values)) + ": " + str(sum(ints)))

if __name__ == "__main__":
    name = "input/regex_sum_1353131.txt"
    solution_1_calc_numbers_from_file(name)
    solution_2_calc_numbers_from_file(name)