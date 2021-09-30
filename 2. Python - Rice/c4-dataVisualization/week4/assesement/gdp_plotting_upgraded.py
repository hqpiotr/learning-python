"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import csv
import math
import pygal

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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            result[rowid] = row
    return result


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    result = {}
    codes_dict = read_csv_as_nested_dict(codeinfo["codefile"], codeinfo["plot_codes"], \
                                            codeinfo["separator"], codeinfo["quote"])
    for plot_code in codes_dict:
        data_country_code = codes_dict[plot_code][codeinfo["data_codes"]]
        result[plot_code] = data_country_code
    return result


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    dict0 = build_country_code_converter(codeinfo)
    dict1 = {}
    for key in dict0:
        dict1[key.lower()] = dict0[key]
    dict2 = {}
    set1 = set()
    for plot_code in plot_countries:
        mapped_key = plot_code.lower()
        # how to use casefold() function
        if mapped_key in dict1:
            if dict1[mapped_key] not in gdp_countries:
                set1.add(plot_code)
            else:
                dict2[plot_code] = dict1[mapped_key]
    return dict2, set1


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    not_found_set = set()
    no_data_set = set()
    lowercase_dict = {key.lower(): value for key, value in build_country_code_converter(codeinfo).items()}

    gdp_data_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_code"],
                                            gdpinfo["separator"], gdpinfo["quote"])
    country_codes = reconcile_countries_by_code(codeinfo, plot_countries, gdp_data_dict)

    result_dict = dict()
    for plot_code in plot_countries:
        mapped_key = plot_code.lower()
        if mapped_key in lowercase_dict:
            if lowercase_dict[mapped_key] not in gdp_data_dict:
                not_found_set.add(plot_code)
            else:
                if gdp_data_dict[country_codes[0][plot_code]][year] != "":
                    gdp = float(gdp_data_dict[country_codes[0][plot_code]][year])
                    gdp_value = math.log10(gdp)
                    result_dict[plot_code] = gdp_value
                else:
                    no_data_set.add(plot_code)
        else:
            not_found_set.add(plot_code)
    return result_dict, not_found_set, no_data_set


def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years
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

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")

# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
