import urllib.request
import re
from bs4 import BeautifulSoup

# TODO: read the file from Web, parse numbers and print sum.
# TODO: 2553 is the sum

def parse_without_bs4(link):
    file_all = urllib.request.urlopen(link).read().decode()
    file_single = urllib.request.urlopen(link)
    pattern = re.compile(r'comments.+>(\d+)')

    """version 1"""
    # example: <tr><td>Bowie</td><td><span class="comments">65</span></td></tr>
    print(sum([int(x) for x in re.findall(pattern, file_all)]))


    """version 3"""
    # for line in file_single:
    #     if re.search(pattern, line.decode()):
    #         val = int(re.search(pattern, line.decode().rstrip()).group(1))
    #         result += val
    # print("result:", result)


def playground(string):
    print(string)
    if re.search(r'span class.*>?([0-9]+)', string) is not None:
        pattern1 = str(re.search(r'span class.*>?([0-9]+)', string).group())
        pattern2 = str(re.search(r'span class.*>?([0-9]+)', string).group(1))
        print("1", pattern1)
        print("2", pattern2)


def using_bs4():
    link = "http://py4e-data.dr-chuck.net/comments_42.html"
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('tr')
    for tag in tags:
        # print(tag.span)

        if re.search(r'\d+',tag.span).group():
            print(str(re.search(r'\d+',tag.span).group()))
            # print(digit)



def main():
    link = "http://py4e-data.dr-chuck.net/comments_42.html"

    parse_without_bs4(link)
    # playground('''<re.Match object; span=(23, 47), match='span class="comments">14'>''')
    # using_bs4()

if __name__ == "__main__":
    main()