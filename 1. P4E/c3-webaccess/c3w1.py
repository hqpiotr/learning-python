# Python Web Access training, part1
# Regexps
import re


def re_search(file):
    regexp = 'From:'
    handle = open(file, 'r')
    no_lines = 0
    for line in handle:
        if re.search(regexp, line):
            line = line.rstrip()
            no_lines += 1
    print('re_search:\t', regexp, '\t=>', no_lines)
    handle.close()

    regexp = '^From: \S+'
    handle = open(file, 'r')
    no_lines = 0
    for line in handle:
        if re.search(regexp, line):  # \S is any non space charater
            line = line.rstrip()
            no_lines += 1
    print('re_search:\t', regexp, '\t=>', no_lines, '\n')


def re_findall(regexp, string):
    list = re.findall(regexp, string)
    print('re_findall: ' + regexp + '\t', '|| input:\t', string, '|| output:\t', list)


def print_explanations():
    print('https://docs.python.org/3/library/re.html\n')
    print('ab+\t 1 or more occurences of b\t || accepted: ab abbb\t || not accepted: a')
    print('ab*\t 0 or more occurences of b\t || accepted: a ab abbbb\t || not accepted: -')
    print('ab?\t 0 or 1 occurences of b\t\t || accepted: a ab\t || not accepted: abb')
    print('\*\+\?\t greedy, use ?suffix to mathch minimal fashion, example: <.*?> matches: \'<a>\', not matches: \'<a> <b> <c>\'')
    print('a{6}\t matches the {6} occurences of \'a\', not less')
    print('a{3,5}\t matches the {3 to 5} occurences of \'a\', not more or less. If 5 a, 5 will be returned')
    print('a{3,5}?\t matches the MINMAL of {3 to 5} occurences of \'a\', not more or less. If 5 a, 3 only will be returned')
    print('[] is a set\t matches any char [a-zA-Z] or any digit [0-9]')
    print('[+*)(]\t special chars lose their meaning if used in set. So direct mapping to those chars is searched')
    print('[AEIOU] is a set\t matches any of the chars inside')
    print('[^AEIOU] is a set\t ^ negates all the chars: return if NOT having these (must be first char in set)')

    print('\n() parenthesis in searching specify start and stop of a match: \'^From (\S+@\S+)\' will not return the "^From" part')
"""
def greedy_matching(string):
    result = re.findall('^F.+:', string)
    print('[greedy_match]:\t\talways results in maximum possible string', result)

def non_greedy(string):
    print("null")
"""

def cheat_sheet():
    return "Python Regular Expression Quick Guide\n\
    ^        Matches the beginning of a line\n\
    $        Matches the end of the line\n\
    .        Matches any character\n\
    \s       Matches whitespace\n\
    \S       Matches any non-whitespace character\n\
    *        Repeats a character zero or more times\n\
    *?       Repeats a character zero or more times (non-greedy)\n\
    +        Repeats a character one or more times\n\
    +?       Repeats a character one or more times (non-greedy)\n\
    [aeiou]  Matches a single character in the listed set\n\
    [^XYZ]   Matches a single character not in the listed set\n\
    [a-z0-9] The set of characters can include a range\n\
    (        Indicates where string extraction is to start\n\
    )        Indicates where string extraction is to end\n"

def main():
    filename = "..\c2-structures\input\input_spammers.txt"
    # re_search(filename)
    # re_findall('[0-9]+', "My 2 favorite numbers are: 19 and 42.")
    # re_findall('ab+', '8zaba a aba caba daba aabb abbbbb KONIEC')
    # greedy_matching("From: John Doe sent on Thursday 08th with: HELLO")
    print_explanations()
    # print(cheat_sheet())

if __name__ == "__main__":
    main()
