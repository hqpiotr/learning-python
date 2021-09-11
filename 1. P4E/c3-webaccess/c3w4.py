# beautiful soup
import urllib.request
from bs4 import BeautifulSoup
import re

def parse_html_using_soup(web_address):
    html = urllib.request.urlopen(web_address).read()
    soup = BeautifulSoup(html, features="html.parser")

    # Get all links prefixed with <a href="..."
    soup_list = soup('a')
    for s in soup_list:
        x = s.get('href', None)
        if re.search(r'^/hqpiotr/.*', x):
            print(x)


if __name__ == "__main__":
    # parse_html_using_soup('http://www.dr-chuck.com/page1.htm')
    parse_html_using_soup('https://github.com/hqpiotr?tab=repositories')