"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import collections
import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, "rt", newline='') as file:
        csvreader = csv.DictReader(file,
                                   skipinitialspace=False,
                                   delimiter=separator,
                                   quotechar=quote)
        headers = list(csvreader.fieldnames)

    # print(headers)
    return headers


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    list_of_dicts = []
    with open(filename, "rt", newline='') as file:
        csvreader = csv.DictReader(file, skipinitialspace=False,
                                   delimiter=separator,
                                   quotechar=quote)

        for row in csvreader:
            list_of_dicts.append(row)
            # OK: WORKING 4 lines, but commented
            # nested_row_dict = {}
            # for col in range(len(csvreader.fieldnames)):
            #     nested_row_dict[csvreader.fieldnames[col]] =\
            #         nested_row_dict.get(csvreader.fieldnames[col], col)
            # list_of_dicts.append(nested_row_dict)
    return list_of_dicts

"""
ERROR:
[-20.0 pts] read_csv_as_list_dict('table1.csv', ',', '"') expected 
[OrderedDict([('Field1', '1'), ('Field2', '2'), ('Field3', '3'), ('Field4', '4')]), 
OrderedDict([('Field1', '5'), ('Field2', '6'), ('Field3', '7'), ('Field4', '8')]), 
OrderedDict([('Field1', '9'), ('Field2', '10'), ('Field3', '11'), ('Field4', '12')])] but received [{'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3}, {'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3}, {'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3}]
but received 
[
    {'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3},
    {'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3}, 
    {'Field1': 0, 'Field2': 1, 'Field3': 2, 'Field4': 3}]
"""

# TODO: not needed
def print_list_of_dicts(table):
    for row, value in enumerate(table):
        print("row", row, end=':\t')
        for k, v in value.items():
            print(k, ":", v, sep='', end=' ')
        print()

def print_list_of_dicts_v2(table):
    for row in table:
        print(row)



def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    big_dict = {}
    with open(filename, "rt") as file:
        csvreader = csv.DictReader(file,
                                   skipinitialspace=False,
                                   delimiter=separator,
                                   quotechar=quote)
        for line in csvreader:
            big_dict[line[keyfield]] = line
    # print(big_dict)
    return big_dict

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')


# TODO: testing
def print_nested_dict(table):
    print("City                ", end='')
    for m in MONTHS:
        print(f'{m:>4}', end='')
    print('\n' + '-' * 64)

    for key, value in table.items():
        print(f'{key:<20}', end='')
        for m in MONTHS:
            print(f'{value[m]:>4}', end='')
        print("")


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        for row in table:
            # csv_writer.writerow(table[row])
            csv_writer.writerow(row)


# Testing #1
# read_csv_fieldnames('table1.csv', ',', '"')
# read_csv_fieldnames('table2.csv', ',', '"')
# read_csv_fieldnames('table3.csv', ',', "'")
# read_csv_fieldnames('table4.csv', ',', '"')
# read_csv_fieldnames('table5.csv', ',', '"')


# Testing #2
t_l_d = read_csv_as_list_dict('hightemp.csv', ',', '"')
# print_list_of_dicts(t_l_d)
print_list_of_dicts_v2(t_l_d)
# t_l_d = read_csv_as_list_dict('table2.csv', ',', '"')
# t_l_d = read_csv_as_list_dict('table3.csv', ',', "'")
# t_l_d = read_csv_as_list_dict('table4.csv', ',', '"')
# t_l_d = read_csv_as_list_dict('table5.csv', ',', '"')
# print_list_of_dicts_v2(t_l_d)
# print(t_l_d)

# Testing #3
# n2d = read_csv_as_nested_dict('hightemp.csv', 'City', ",", '"')
# print_nested_dict(n2d)

# Testing #4
# name = 'table1.csv'
# fieldnames = read_csv_fieldnames(name, ',', '"')
# mytable = read_csv_as_list_dict(name, ',', '"')
# print(mytable)
# write_csv_from_list_dict('output.csv', mytable, fieldnames, ',', '"')