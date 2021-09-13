# SOUP HTML parser
import re
import urllib.request
from bs4 import BeautifulSoup

"""
    get the chain of names, using as input (1) amount of hops and (2) the position 
    of the link on each site. Example: 4, 3 => iterate 4 times, get 3rd from each 
    site, remember the link, output a resulting name. Example below:
     <li style=: 16px;"><a href="http://py4e../known_by_Aniqa.html">Aniqa</a></li>
"""

def dostuff(link):
    print('Analyzing URL: ', 'http://py4e-data.dr-chuck.net/known_by_Ilyas.html')
    amount_of_hops = int(input('Enter count: '))
    number_in_sequence = int(input('Enter position: '))
    nextlink = link
    finalname = ""

    for hop in range(amount_of_hops):
        file = urllib.request.urlopen(nextlink)
        soup = BeautifulSoup(file, "html.parser")
        index = 0

        for a in soup('a'):
            index += 1
            if index == number_in_sequence:
                href = a.get("href")
                print("Retrieving:", href)
                nextlink = href
                break
            else:
                continue
        finalname = re.search(r'known_by_(\w+).html', nextlink).group(1)
    print("\nAnswer is:", finalname)


if __name__ == "__main__":
    webpage_test = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    webpage_check = "http://py4e-data.dr-chuck.net/known_by_Ilyas.html"
    # dostuff(webpage_test)
    dostuff(webpage_check)
