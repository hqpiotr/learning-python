# JSON
import json
import urllib.request, urllib.parse

"""
    The program will prompt for a location, contact a web service and retrieve
    JSON for the web service and parse that data, and retrieve the first
    place_id from the JSON. A place ID is a textual identifier that uniquely
    identifies a place as within Google Maps.

    -- API End Points: --
    To complete this assignment, you should use this API endpoint that has a
    static subset of the Google Data:
"""

def do_API_search():
    address = input("Enter location: ")
    apiurl = "http://py4e-data.dr-chuck.net/json?"

    params = {}
    params['address'] = address
    params['key'] = 42

    myurl = apiurl + urllib.parse.urlencode(params)
    print("Getting: ", myurl)
    webcontent = urllib.request.urlopen(myurl).read().decode()
    print("Received: ", len(webcontent), "bytes/chars.")

    try:
        tree = json.loads(webcontent)
    except:
        print("error loading content to json")
        tree = None


    if not tree or 'status' not in tree or tree['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(webcontent)


    # print(json.dumps(tree, indent=4))
    print(tree['results'][0]['place_id'])
    # print('"'+ str(x) + ':' + str(y) + '"')





if __name__ == "__main__":
    do_API_search()