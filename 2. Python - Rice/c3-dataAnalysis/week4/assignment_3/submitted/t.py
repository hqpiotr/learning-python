"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import csv
YEAR = 2006

# moved to here.
baseballdatainfo = {
                    # "masterfile": "Master_2016.csv",   # Name of Master CSV file
                    "masterfile": "testing_csv/master2.csv",   # Name of Master# CSV file
                    # "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                    "battingfile": "testing_csv/batting2.csv", # Name of Batting CSV # file
                    "separator": ",",                  # Separator character in CSV files
                    "quote": '"',                      # Quote character in CSV files
                    "playerid": "playerID",            # Player ID field name
                    "firstname": "nameFirst",          # First name field name
                    "lastname": "nameLast",            # Last name field name
                    "yearid": "yearID",                # Year field name
                    "atbats": "AB",                    # At bats field name
                    "hits": "H",                       # Hits field name
                    "doubles": "2B",                   # Doubles field name
                    "triples": "3B",                   # Triples field name
                    "homeruns": "HR",                  # Home runs field name
                    "walks": "BB",                     # Walks field name
                    "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}



def print_nested_dict(table):
    """
    Function for printing dict.
    Input:
        - list of dicts
    Output:
        - none, print
    """
    for key, value in table.items():
        print(f'{key:<12} {value}', end="\n")


def print_list_of_dicts(table):
    """
    Function to list the contents
        Input:
            data table
        Output:
            print the data table
    """
    for value in table:
        print(value, end='\n')


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

    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)

        if 'playerid' not in csvreader.fieldnames and 'playerID' not in csvreader.fieldnames:
            baseballdatainfo['playerid'] = 'player'
            baseballdatainfo['firstname'] = 'firstname'
            baseballdatainfo['lastname'] = 'lastname'
            baseballdatainfo['yearid'] =  'year'
            baseballdatainfo['atbats'] =  'atbats'
            baseballdatainfo['hits'] = 'hits'
            baseballdatainfo['doubles'] = 'doubles'
            baseballdatainfo['triples'] = 'triples'
            baseballdatainfo['homeruns'] = 'homers'
            baseballdatainfo['walks'] = 'walks'
            baseballdatainfo['battingfields'] = \
                            ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']
            # print("SWAPPED OUT!\n")

    return table


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
    table = {}
    overwritten_key = keyfield

    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)

        # print("fieldnames:", csvreader.fieldnames)
        if 'playerid' not in csvreader.fieldnames and 'playerID' not in csvreader.fieldnames:
            baseballdatainfo['playerid'] = 'player'
            baseballdatainfo['firstname'] = 'firstname'
            baseballdatainfo['lastname'] = 'lastname'
            baseballdatainfo['yearid'] = 'year'
            baseballdatainfo['atbats'] = 'atbats'
            baseballdatainfo['hits'] = 'hits'
            baseballdatainfo['doubles'] = 'doubles'
            baseballdatainfo['triples'] = 'triples'
            baseballdatainfo['homeruns'] = 'homers'
            baseballdatainfo['walks'] = 'walks'
            baseballdatainfo['battingfields'] = []
            # print("AGAIN... SWAPPED OUT!\n")

            overwritten_key = baseballdatainfo['playerid']
            # print(overwritten_key)

        for row in csvreader:
            rowid = row[overwritten_key]
            table[rowid] = row
    return table


# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


## Part 1: Functions to compute top batting statistics by year

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    # WAS working until called: # filter_by_year([{'year1': '1', 'year2': '2',
    # 'year3': '3'}], 1, 'year1')
    # result = []
    # for line in statistics:
    #     for v in line.values():
    #         if v == str(yearid):
    #             result.append(line)

    # for i in statistics:
    #     print('stat=', i)
    # print('stat=',statistics)
    # print('year=',year)
    # print('yearid',yearid)
    # NEW:
    result = []
    for line in statistics:
        # print('line[yearid]=',line[yearid])
        if line[yearid] == str(year):
            result.append(line)
    return result

def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    players = []
    # print(statistics)
    for line in statistics:
        # print(line)
        # players.append((line['playerID'], formula(baseballdatainfo, line)))
        # players.append(line[info['playerid']], formula(baseballdatainfo, line))
        # print(line[info['playerid']])
        players.append((line[info['playerid']], formula(baseballdatainfo, line)))
    players.sort(key=lambda pair: pair[1], reverse=True)
    return players[:numplayers]

def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    master_table = read_csv_as_nested_dict(info['masterfile'],
                                           info['playerid'],
                                           info['separator'],
                                           info['quote'])

    # for k,v in master_table.items():
    #     print(k,v)
    # print(master_table) # Fishy
    #
    # print("TOP IDs: ", top_ids_and_stats)
    res_strings = []
    for pair in top_ids_and_stats:
        for each_key in master_table:
            if pair[0] == each_key:
                # print("FOUND! pair[0]=", pair[0], " each_key=", each_key)
                # print("master [each_key] = ", master_table[each_key][info['firstname']])
                single_string = '' + str(f'{pair[1]:.3f}') + ' --- ' + \
                                master_table[each_key][info['firstname']] + \
                                ' ' + master_table[each_key][info['lastname']]
                res_strings.append(single_string)

    return res_strings

def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    # WAS:
    data = read_csv_as_list_dict(info['battingfile'],
                                 info['separator'],
                                 info['quote'])

    filtered_year =  filter_by_year(data, year, info['yearid'])
    top_players = top_player_ids(info, filtered_year, formula, numplayers)
    names = lookup_player_names(info, top_players)

    # print("AFTER ALL: ", baseballdatainfo)
    return names


## Part 2: Functions to compute top batting statistics by career

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    aggregate = {}
    for item in statistics:
        if not item[playerid] in aggregate:
            aggregate[item[playerid]] = {playerid: item[playerid]}
            for field in fields:
                aggregate[item[playerid]][field] = 0
        for field in fields:
            value = int(item[field])
            aggregate[item[playerid]][field] += value
    return aggregate


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    csv_input = read_csv_as_list_dict(info["battingfile"],
                                     info["separator"],
                                     info["quote"])
    aggr_stats_dict = aggregate_by_player_id(csv_input, info["playerid"],
                                             info["battingfields"])
    aggr_stats = list(aggr_stats_dict.values())
    top_ids = top_player_ids(info, aggr_stats, formula, numplayers)
    list_of_strings = lookup_player_names(info, top_ids)
    return list_of_strings


## Provided testing code

def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    # moved from here.

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

#test_baseball_statistics()


