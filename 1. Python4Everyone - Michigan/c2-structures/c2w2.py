# 2. file operations

def count_file_lines(filename):
    amount = 0
    filehandle = open(filename, 'r')
    for line in filehandle:
        amount += 1
    return amount

def from_course_test(inputfile):
    stringcount = 0
    floatval = 0.0

    try:
        handle = open(inputfile, 'r')
        content = handle.read()
    except:
        print('no such file, quitting')
        quit()

    for line in handle:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            stringcount += 1
            startpos = line.find(':')
            stringval = line[startpos + 2:startpos + 8]
            floatval += float(stringval)
    print('Average spam confidence:', floatval / stringcount)

def print_x_chars_from_file(filename, x):
    return open(filename, 'r').read(x)

def print_x_lines_from_file(filename, x):
    handle = open(filename, 'r')
    n = 0
    for i in handle:
        if not i.isspace():
            i = i.strip()
            if n < x:
                n += 1
                print(i)


# main testing
def mock_test_all():
    firstfile = "input/input_mail.txt"
    print(count_file_lines(firstfile))
    print_x_lines_from_file(firstfile, 5)
    print(print_x_chars_from_file(firstfile, 130))

    secondfile = "input/input_spammers.txt"
    count_file_lines(secondfile)
    print('DONE')

if __name__ == "__main__":
    mock_test_all()
    

