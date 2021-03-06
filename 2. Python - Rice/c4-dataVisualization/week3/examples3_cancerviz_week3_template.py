"""
Week 3 practice project template for Python Data Visualization
Read two CSV files and join the resulting tables based on shared FIPS codes
Analyze both data sources for anamolous FIPS codes
"""

import csv



#########################################################
# Provided code for week 3

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table



def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)



# Part 1 - function that creates a dictionary from a table

def make_dict(table, key_col):
    """
    Given a 2D table (list of lists) and a column index key_col,
    return a dictionary whose keys are entries of specified column
    and whose values are lists consisting of the remaining row entries
    """
    # for row in table:
    #     list_row = []
    #     for index, col in enumerate(row):
    #         list_row.append(col)
    #         if index == key_col:
    #             dict[col] = list_row
    #             list_row.pop(index)
    # return dict
    result = {}
    for row in table:
        key = row[key_col]
        list_row = list(row)
        list_row.pop(key_col)
        result[key] = list_row
    return result



def test_make_dict():
    """
    Some tests for make_dict()
    """
    table1 = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
    print(make_dict(table1, 0))
    print(make_dict(table1, 1))
    print(make_dict(table1, 2))
    table2 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    print(make_dict(table2, 1))
    print(make_dict(table2, 2))
    
# test_make_dict()



# Part 2 - script for merging the CSV files

CANCER_FIPS_COL = 2
CENTER_FIPS_COL = 0


def merge_csv_files(cancer_csv_file, center_csv_file, joined_csv_file):
    """
    Read two specified CSV files as tables
    Join the these tables by shared FIPS codes
    Write the resulting joined table as the specified file
    Analyze for problematic FIPS codes
    """
    # Read in both CSV files
    cancer_data = read_csv_file(cancer_csv_file)
    center_data = read_csv_file(center_csv_file)

    cancer_FIPS_list = [cancer_data[index][CANCER_FIPS_COL] for index in range(len(cancer_data))]
    center_FIPS_list = [center_data[index][CENTER_FIPS_COL] for index in range(len(center_data))]
    print("got ", len(cancer_FIPS_list), " codes from CANCER.")
    print("got ", len(center_FIPS_list), " codes from CENTER.")

    intersected_FIPS = list(sorted(set(cancer_FIPS_list).intersection(center_FIPS_list)))
    print("common: ", len(intersected_FIPS))
    diffs = [x for x in cancer_FIPS_list if x not in center_FIPS_list]
    print("\ndiffs (", len(diffs), ")", diffs)

    joined_data = []
    same_FIPS_found = 0

    for first in range(len(cancer_data)):
        for second in range(len(center_data)):
            if cancer_data[first][CANCER_FIPS_COL] == center_data[second][CENTER_FIPS_COL]:
                combined_row = cancer_data[first]
                combined_row.extend(center_data[second][1:])
                joined_data.append(combined_row)

                same_FIPS_found += 1
                break

    # print("I found: ", same_FIPS_found, " same FIPS indexes.")
    write_csv_file(joined_data, joined_csv_file)

    # Compute joined table, print warning about cancer-risk FIPS codes that are not in USA map
    # Write joined table
    # Print warning about FIPS codes in USA map that are missing from cancer risk data
    pass



merge_csv_files("cancer_risk_trimmed_solution.csv", "USA_Counties_with_FIPS_and_centers.csv", "outcome_joined.csv")




## Part 3 - Explanation for anomalous FIPS codes

## https://www1.udel.edu/johnmack/frec682/fips_codes.html
##
## Output anamolies for cancer risk data
## Puerto Rico, Virgin Island, Statewide, Nationwide - FIPS codes are all not present on USA map
## One specific county (Clifton Forge, VA - 51560) is also not present in USA map.
## According URL above, Clifton Forge was merged with another VA county prior to 2001
##
## Output anamolies for USA map
## State_Line, separator - FIPS codes are all not present in cancer-risk data
## One specific county (Broomfield County - 08014) is also not present in cancer-risk data
## Accoring to URL above, Broomfield County was created in 2001
##
## Implies cancer risk FIPS codes were defined prior to 2001, the USA map FIPS codes were defined after 2001
