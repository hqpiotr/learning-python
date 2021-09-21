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
    line1 = line1.rstrip()
    line2 = line2.rstrip()

    if idx >= 0:
        output = line1 + "\n" + "=" * idx + "^\n" + line2 + "\n"
    else:
        output = ""
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
    index = IDENTICAL
    len1 = len(line1)
    len2 = len(line2)

    if len1 != 0 and len2 != 0:
        for first in range(len1):
            if index != IDENTICAL:
                break

            for second in range(len2):
                if index != IDENTICAL:
                    break
                if first == second or (first == min(len1, len2) and len1 != len2):
                    if line1[first] != line2[second] and index == IDENTICAL:
                        index = first
                        break

    if index == IDENTICAL and len1 != len2:
        index = min(len1, len2)

    return index


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
    with open(filename, "rt") as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
    return lines


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
    len1 = len(lines1)
    len2 = len(lines2)

    if len1 != 0 and len2 != 0:
        for line_number in range(len(lines1)):
            if singleline_diff(lines1[line_number], lines2[line_number]) != IDENTICAL:
                return line_number, singleline_diff(lines1[line_number], lines2[line_number])
    else:
        return 0, 0
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
    else:
        output = "Line " + str(result[0]) + ":\n"
        # output += singleline_diff_format(lines1[result[0]], lines2[result[0]], result[1])
        if not lines1:
            output += singleline_diff_format("", lines2[result[0]], result[1])
            # output = output + "\n" + lines2[result[0]] + str(result[1])
        elif not lines2:
            output += singleline_diff_format(lines1[result[0]], "", result[1])
            # output = output + lines1[result[0]] + "\n" + str(result[1])
        else:
            output += singleline_diff_format(lines1[result[0]], lines2[result[0]], result[1])
            # output = output + lines1[result[0]] + lines2[result[0]] + str(result[1])

    return output




if __name__ == "__main__":
    filename1 = "input_filediff/file1.txt"
    filename2 = "input_filediff/file2.txt"
    filename3 = "input_filediff/file3.txt"
    filename8 = "input_filediff/file8.txt"
    filename9 = "input_filediff/file9.txt"

    # 1: String checking
    # string1 = 'abcdefg'
    # string2 = 'abc'
    # diff = singleline_diff(string1, string2)
    # print(singleline_diff_format(string1, string2, diff))

    # 2: Single line file checking
    # file1 = open(filename9, "rt")
    # file2 = open(filename8, "rt")
    #
    # for line1 in file1:
    #     for line2 in file2:
    #         diff = singleline_diff(line1, line2)
    #         if diff == IDENTICAL:
    #             break
    #         else:
    #             print(singleline_diff_format(line1, line2, diff))
    #             break
    # file1.close()
    # file2.close()

    # 3: Multi line file checking
    # lines1 = get_file_lines(filename2)
    # lines2 = get_file_lines(filename1)

    lines3 = ['line1', 'line2']
    lines4 = ['line1', 'line2', 'line3']
    result = multiline_diff(lines3, lines4)
    print(result)
    # if result is not (IDENTICAL, IDENTICAL):
    #     print(file_diff_format(filename2, filename1))
