# XML
import xml.etree.ElementTree as ET

smalldata = '''
<people>
    <person>
        <name>testing</name>
        <age>11</age>
    </person>
    <person>
        <name>completed</name>
        <age>22</age>
    </person>
</people>
'''

data = ''' <stuff>
    <people>
        <person p="1">
             <name>Stas</name>
             <age>37</age>
             <phone mobile="true">555 344 211</phone>
             <email hide="yes"/>
        </person>
        <person p="2">
             <name>Nel</name>
             <age>19</age>
             <phone mobile="true">0800 772 772</phone>
             <email hide="yes"/>
        </person>
    </people>
</stuff>
'''

small_tree = ET.fromstring(smalldata)
big_tree = ET.fromstring(data)
print('small data, name: ', small_tree.find('person/name').text)

list = big_tree.findall('people/person')
print(len(list))
for x in list:
    print('name: ', x.find('name').text)