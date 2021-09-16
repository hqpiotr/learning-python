# JSON

import json
import urllib.request

"""
   The program will prompt for a URL, read the JSON data from that URL using 
   urllib and then parse and extract the comment counts from the JSON data,
   compute the sum of the numbers in the file and enter the sum below
"""
"""
    raw data example
        {
          "note":"This file contains the sample data for testing",
          "comments":[
            {
              "name":"Romina",
              "count":97
            },
            {
              "name":"Laurie",
              "count":97
            },
            ...
        }
"""


def dostuff(link):
    file = urllib.request.urlopen(link).read().decode()
    data = json.loads(file)
    # print(json.dumps(data, indent=2))
    print(sum([int(x['count']) for x in data['comments']]))


if __name__ == "__main__":
    link_test = "http://py4e-data.dr-chuck.net/comments_42.json"  # 2553
    link_final = "http://py4e-data.dr-chuck.net/comments_1353136.json"
    # dostuff(link_test)
    dostuff(link_final)
