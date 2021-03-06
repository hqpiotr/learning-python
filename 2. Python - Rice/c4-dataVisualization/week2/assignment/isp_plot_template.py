"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import csv
import pygal
import random



def print_some_examples_from_csv(sourcetable, amount, country=None):
    """
    Function takes the table with sample amount of countries to print
    :param sourcetable: dictionary input
    :param amount: number of countries to sample printout 
    :param country: optional, for printing only one country if needed
    :return: nothing is returned, printing function only
    """
    countries_counter = 0
    for key, value in sourcetable.items():
        output = ('{:<20} {:>5} {:>5} {:>15} {:>12} {:>12} {:>12} {:>12} \
                {:>12} {:>12}'.format(key,
                  value['Country Code'],
                  value['Indicator Name'],
                  value['Indicator Code'],
                  value['2000'],
                  value['2001'],
                  value['2002'],
                  value['2003'],
                  value['2004'],
                  value['2005']))
        if country is None and countries_counter < amount:
            print(output)
            countries_counter += 1
        elif key == country:
            print(output)
            break
    print("-" * 138)

def print_tuples_nl(data):
    """
    Function to print tuple () data only
    :param data: input source as pair of tuples
    :return: nothing, printing only
    """
    for item in data:
        print("\t( " + str(item[0]) + ", " + str(item[1]) + " )")

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    result = {}
    with open(filename, "rt") as file:
        csvreader = csv.DictReader(file, delimiter=separator, quotechar=quote)
        for line in csvreader:
            result[line[keyfield]] = line
    return result

def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.
    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    # years = [x for x in range(int(gdpinfo['min_year']), int(gdpinfo['max_year']) + 1)]
    years = list(range(int(gdpinfo['min_year']), int(gdpinfo['max_year']) + 1))
    tuples = []

    # TODO: Alternatively, use list comprehension:
    tuples = [(int(year), float(gdpdata[country])) for year in years for country in gdpdata if country == str(year) and gdpdata[country] != '']

    # for country in gdpdata:
    #     if country != 'Not classified':
    #         for year in years:
    #             if country == str(year):
    #                 if gdpdata[country] != '':
    #                     tuples.append((int(year), float(gdpdata[country])))
    return tuples


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    gdp_data = read_csv_as_nested_dict(gdpinfo['gdpfile'],
                                       gdpinfo['country_name'],
                                       gdpinfo['separator'],
                                       gdpinfo['quote'])
    dict_country_coords = {}

    for country in country_list:
        dict_country_coords[country] = []
        for key, value in gdp_data.items():
            if key == country:
                tup = build_plot_values(gdpinfo, gdp_data[country])
                dict_country_coords[country] = tup
            else:
                continue
    return dict_country_coords


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """

    data = build_plot_dict(gdpinfo, country_list)
    xy_chart = pygal.XY(title="GDP per country throughout the years",
                        x_title="Year",
                        y_title="Gross Domestic Product")

    # TODO: Alternatively, use list comprehension:
    #   - condition:
    #       - if key from dict is a country
    #   - two loops,
    #       - external: for each country
    #       - internal: for each element in dictionary {country + (x_coord, y_coord)}
    #   - return:
    #       - tuple which is being added to chart, for specific country, per each year
    country_coords = [xy_chart.add(country, v) for k, v in data.items() for country in country_list if k == country]

    # for country in country_list:
    #     for k,v in data.items():
    #         if k == country:
    #             country_coords = v
    #             print(f'{country:<30}{country_coords}')
    #             xy_chart.add(country, country_coords)
    #             break

    xy_chart.render_in_browser()
    xy_chart.render_to_file(plot_file)

    return


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    SAMPLE_NUMBER_OF_COUNTRIES = 10
    # SAMPLE_NUMBER_OF_YEAR_TUPLES = 10
    csvdata = read_csv_as_nested_dict(gdpinfo['gdpfile'], 'Country Name', gdpinfo['separator'], gdpinfo['quote'])
    countries_only_csvdata = list(csvdata.keys())
    random.shuffle(countries_only_csvdata)
    countries_only_csvdata = countries_only_csvdata[:SAMPLE_NUMBER_OF_COUNTRIES]
    print(countries_only_csvdata)

    # render_xy_plot(gdpinfo, ["United Kingdom", "United States"], "_my_chart_uk+usa.svg")
    render_xy_plot(gdpinfo, countries_only_csvdata, "_my_chart_big.svg")
    # render_xy_plot(gdpinfo, ['Poland', 'Germany', 'Czech Republic', 'Slovakia', 'United Kingdom'], "_my_chart_big.svg")


test_render_xy_plot()

