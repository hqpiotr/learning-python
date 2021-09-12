import urllib.request
import re
from bs4 import BeautifulSoup
import requests
# TODO: read the file from Web, parse numbers and print sum.


def playground(string):
    print(string)
    searchfor = re.compile(r'(comments.+>)?(\d+)')
    if re.search(searchfor, string) is not None:
        pattern1 = str(re.search(searchfor, string).group())
        pattern2 = str(re.search(searchfor, string).group(1))
        pattern3 = str(re.search(searchfor, string).group(2))
        print(pattern1)
        print(pattern2)
        print(pattern3)


def parse_without_bs4(link):
    file = urllib.request.urlopen(link)
    pattern = re.compile(r'comments.+>(\d+)')

    """version 1"""
    # TODO: list comprehension
    # print("v1:\t" + str(sum([int(x) for x in re.findall(pattern, file.read().decode())])))

    """version 2"""
    result = 0
    for line in file:
        if re.search(pattern, line.decode()):
            val = int(re.search(pattern, line.decode().rstrip()).group(1))
            result += val
    print("v2:\t" + str(result))


def using_bs4(link):
    """         example of using requests """
            # page = requests.get(link) # import requests
            # print(page.content.decode())
            # soup_req = BeautifulSoup(page.content, "html.parser")

    url = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(url, "html.parser")

    """version 1"""
    # TODO: list comprehension
    print(sum([int(re.search(r'\d+', x.decode()).group()) for x in soup('span')]))
    # print(sum([int(re.search(r'\d+', str(x)).group()) for x in soup('span')])) # also works

    """version 2"""
    # digit, overall = 0, 0
    # values = soup('span')
    # for v in values:
    #     digit = re.search(r'\d+', v.decode()).group() # or decode it to string
    #     print(v.decode() + "\t\t\t" + digit)
    #     overall += int(digit)
    # print("\nsum:", overall)


def main():
    link = "http://py4e-data.dr-chuck.net/comments_42.html"
    longer_link = "http://py4e-data.dr-chuck.net/comments_1353133.html"
    # playground('''<tr><td>Bowie</td><td><span class="comments">65</span></td></tr>''')
    # using_bs4(link)
    parse_without_bs4(link)
    # using_bs4(longer_link)

if __name__ == "__main__":
    main()