# 1. basics

def min_max_values(array):
    min = None
    max = None
    for n in array:
        if min is None:
            min = n
        if max is None:
            max = n
        if n > max:
            max = n
        elif n < min:
            min = n
    print('min:', min, 'max:', max)

def spelling(s_word):
    for s_letter in s_word:
        print(s_letter)

def counting(c_word, c_letter):
    count = 0
    for x in c_word:
        if x == c_letter:
            count += 1
    return count

def slicing(sl_word, middle, last):
    print('slicing:', sl_word[0:middle], '-', sl_word[middle:last])

def containing(cont_word, cont_letter):
    if cont_letter in cont_word:
        return True

def playing_with_strings(s_input):
    print(s_input.upper())

def get_hostname(line):
    atposition = line.find('@')
    # search from '@' sign till space
    endposition = line.find(' ', atposition)
    address = line[atposition+1: endposition]
    return address

"""
------------------------------------------------
tests
------------------------------------------------
"""

def mock_test_min_max():
    print('-------> 1:')
    array = [0, 3, -5, 37, 9, 11]
    min_max_values(array)

def mock_test_spelling(input_word):
    print('-------> 2:')
    spelling(input_word)

def mock_test_counting(parameter_word, parameter_letter):
    print('-------> 3:')
    print('how many ', parameter_letter, 'in word:', parameter_word, counting(parameter_word, parameter_letter))

def mock_test_slicing(input_word, input_letter):
    print('-------> 4:')
    print('count', input_letter, 'in', input_word, counting(input_word, input_letter))
    slicing(input_word, 3, 10)

def mock_test_containing(test_word, test_letter):
    print('-------> 5:')
    print('Is ', test_word, 'containing letter:', test_letter, '? -->', containing(test_word, test_letter))

def mock_test_hostname(in_address):
    print('-------> 6:')
    print('From this line:', in_address, 'the host is: ', get_hostname(in_address))


# main testing
def mock_test_all():
    # already tested
    mock_test_min_max()
    mock_test_spelling('mama banana')
    mock_test_counting('zdziszlaw', 'z')
    mock_test_slicing('mama banana', 'a')
    mock_test_containing('mama banana', 'b')
    mock_test_hostname('From name.surname@company.com.pl at 8th of Sep 2020')
    print('DONE')

if __name__ == "__main__":
    mock_test_all()
    

