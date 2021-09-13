# XML
import urllib.request
import xml.etree.ElementTree as ET

""" 
    the program will prompt for a URL, read the XML data from that URL using
    urllib and then parse and extract the comment counts from the XML data,
    compute the sum of the numbers in the file.
"""

def test_string(input):
    tree = ET.fromstring(input)
    """ XP method: check all paths using .// """
    print(sum([int(x.text) for x in tree.findall('.//count')]))
    """ main usage: section/subsection"""
    # print(sum([int(x.find('count').text) for x in tree.findall('comments/comment')]))


def test_file(input):
    file = open(input).read()
    tree = ET.fromstring(file)
    print(sum([int(x.text) for x in tree.findall('.//count')]))


def test_online(input):
    file = urllib.request.urlopen(input).read().decode()
    tree = ET.fromstring(file)
    print(sum([int(x.text) for x in tree.findall('.//count')]))


if __name__ == "__main__":
    string_input = '''
    <commentinfo>
      <note>This file contains the sample data for testing</note>

        <comments>
            <comment>
               <name>Romina</name>
               <count>2500</count>
            </comment>
            <comment>
               <name>Laurie</name>
               <count>50</count>
            </comment>
            <comment>
               <name>Hugh</name>
               <count>3</count>
            </comment>
        </comments>
    </commentinfo>
    '''
    file_input = "input/comments_42.xml"
    web_input_test = "http://py4e-data.dr-chuck.net/comments_42.xml"
    web_input_final = "http://py4e-data.dr-chuck.net/comments_1353135.xml"

    test_string(string_input)
    test_file(file_input)
    test_online(web_input_test)
    test_online(web_input_final)