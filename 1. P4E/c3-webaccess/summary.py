// URL:
import urllib.request
file = urllib.request.urlopen(link).read().decode()
for line in file:
	do stuff.decode()

// BS4:
from bs4 import Beautifulsoup as BS
soup = BS(file, "html.parser")
for line in soup('a')
	href = line.get('href')
	or
	re.search(xxx, line.decode().group())

// XML
import xml.etree.ElementTree as ET
tree = ET.fromstring(file)
tree.find('single/nest')
for line in tree.findall('comments/comment'): # .//count
	line.find('count').text

// JSON
import json
js = json.loads(file)
js['person']
js['age']