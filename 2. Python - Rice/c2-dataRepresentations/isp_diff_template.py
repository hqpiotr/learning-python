"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
IDENTICAL = -1


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    my_line1 = len(line1)
    my_line2 = len(line2)

    if my_line1 >= my_line2:
        if my_line1 < idx < 0:
            return ""
    else:
        if my_line2 < idx < 0:
            return ""

    delimeter = "=" * idx
    delimeter += "^"
    output = line1 + "\n" + delimeter + "\n" + line2 + "\n"
    return output


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    diff_index = -1
    index_of_string = 0

    line1 = line1.strip()
    line2 = line2.strip()

    if len(line1) >= len(line2):
        if len(line1) != 0 and len(line2) != 0:
            for index_of_string in range(len(line1)):
                if index_of_string == len(line2) and len(line1) > index_of_string:
                    diff_index = index_of_string
                    return diff_index
                if line1[index_of_string] == line2[index_of_string]:
                    continue
                else:
                    diff_index = index_of_string
                    # print(singleline_diff_format(line1, line2, diff_index))
                    return diff_index
        else:
            diff_index = 0
            return diff_index
    else:
        if len(line2) != 0 and len(line1) != 0:
            for index_of_string in range(len(line2)):
                if index_of_string == len(line1) and len(line2) > index_of_string:
                    diff_index = index_of_string
                    return diff_index
                if line2[index_of_string] == line1[index_of_string]:
                    continue
                else:
                    diff_index = index_of_string
                    # print(singleline_diff_format(line1, line2, diff_index))
                    return diff_index
        else:
            diff_index = 0
            return diff_index

    # else:
    #     diff_index = len(line2) + 1
    #     return diff_index

    if diff_index == -1:
        return IDENTICAL


def my_test_singleline_diff(my_filename1, my_filename2):
    file1 = open(my_filename1, "rt")
    file2 = open(my_filename2, "rt")

    for line1 in file1:
        for line2 in file2:

            diff = singleline_diff(line1, line2)
            if diff == IDENTICAL:
                # print("IDENTICAL")
                break
            else:
                print(singleline_diff_format(line1, line2, diff))
                # print("NOT IDENTICAL, diff@", diff, "position.")
                break
    file1.close()
    file2.close()


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = ""
    try:
        file = open(filename, "rt")
    except FileNotFoundError as err:
        print(err)

    lines = []
    for line in file:
        lines.append(line.rstrip())
    file.close()

    return lines


def my_test_multilines_diff(multi_filename1, multi_filename2):
    lines1 = get_file_lines(multi_filename1)
    lines2 = get_file_lines(multi_filename2)
    # print("lines1 multiline:", lines1)
    # print("lines2 multiline:", lines2)
    result = multiline_diff(lines1, lines2)

    if result is not (IDENTICAL, IDENTICAL):
        print(file_diff_format(multi_filename1, multi_filename2))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    # TODO: check if file isn't empty
    # if len(lines1) != 0:

    for line_number in range(len(lines1)):
        if singleline_diff(lines1[line_number], lines2[line_number]) != IDENTICAL:
            return line_number, singleline_diff(lines1[line_number], lines2[line_number])
    return IDENTICAL, IDENTICAL


def file_diff_format(f_filename1, f_filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(f_filename1)
    lines2 = get_file_lines(f_filename2)
    result = tuple(multiline_diff(lines1, lines2))

    if result == (IDENTICAL, IDENTICAL):
        output = "No differences\n"
        return output
    else:
        output = "Line " + str(result[0]) + ":\n"
        output += singleline_diff_format(lines1[result[0]], lines2[result[0]], result[1])

    return output


if __name__ == "__main__":
    filename1 = "input_filediff/file1.txt"
    filename2 = "input_filediff/file2.txt"
    filename3 = "input_filediff/file3.txt"
    filename8 = "input_filediff/file8.txt"
    filename9 = "input_filediff/file9.txt"



    string1 = 'abc'
    string2 = 'abcd'
    diff = singleline_diff(string1, string2)
    if diff == IDENTICAL:
        print("No differences")
    else:
        print(singleline_diff_format(string1, string2, diff))
        # print("NOT IDENTICAL, diff@", diff, "position.")

    # my_test_singleline_diff(filename1, filename2)
    # my_test_singleline_diff(filename1, filename3)
    # my_test_singleline_diff(filename3, filename2)

    # my_test_multilines_diff(filename8, filename9)
    # my_test_multilines_diff(filename1, filename2)
    # my_test_multilines_diff(filename3, filename2)
