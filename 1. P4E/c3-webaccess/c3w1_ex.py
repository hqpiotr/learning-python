# input/regex_sum_1353131.txt --> There are 90 values with a sum=445833
# input/regex_sum_42.txt --> There are 69 values and the sum ends with 973
import re


def solution_1_calc_numbers_from_file(filename):
    file = open(filename)
    ints = []

    for line in file:
        strings_list = re.findall('[\d]+', line)
        for word in strings_list:
            ints.append(int(word))
    print('#' + str(len(ints)) + ': ' + str(sum(ints)))


def solution_2_calc_numbers_from_file(filename):
    file = open(filename)
    values = re.findall('[0-9]+', file.read())
    ints = []

    for v in values:
        ints.append(int(v))
    print("#" + str(len(values)) + ": " + str(sum(ints)))


def best_solution(fn):
    # fh = open(fn, 'r')

    # list comprehension: x is every digit in string; make it int; create a list;
    # ints = [int(x) for x in re.findall('[\d]+', fh.read())]
    # print('#' + str(len(ints)) + ': ' + str(sum(ints)))

    print(sum([int(x) for x in re.findall('[0-9]+', open(fn).read())]))

if __name__ == "__main__":
    name = "input/regex_sum_1353131.txt"
    # solution_1_calc_numbers_from_file(name)
    # solution_2_calc_numbers_from_file(name)
    best_solution(name)
