# Python Web Access training, part1
import re

def re_search(file):
    handle = open(file, 'r')
    no_lines = 0
    for line in handle:
        if re.search('From:', line):
            line = line.rstrip()
            no_lines += 1
    print('[re_search]:\tusing .search() line .find(),', no_lines)
    handle.close()

    handle = open(file, 'r')
    no_lines = 0
    for line in handle:
        if re.search('^From:', line):
            line = line.rstrip()
            no_lines += 1
    print('[re_search]:\tusing .search() line .startswith()', no_lines)



def main():
    filename = "..\c2-structures\input\input_spammers.txt"
    re_search(filename)


if __name__ == "__main__":
    main()