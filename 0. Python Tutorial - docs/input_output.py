"""
Python Tutorial docs: https://docs.python.org/3/tutorial/inputoutput.html
"""

############## 1. Formatting strings #############
print('abc\nm')
print("abc\nm")

# r' is for raw string
print(r"a'bc\nm")
print(R'a"bc\nm')

a = 'zx"spectrum'
b = "zx'spectrum"

# f' is for format
print(f'a={a}, b={b}')           # cool!
print('a={}, b={}'.format(a, b),end="\n\n") # also, but more effort!

import math
digits = 21
print(f'PI with: {digits} after comma: {math.pi:>30.{digits}f}.', end='\n')
# 3.14159265358979311599


################ 2. File handling ################
# r - read
# w - write
# a - append
# r+ - read + write

import os
# use with... it closes the file when Exception, and no try/except needed
with open('../sample.txt') as file:
    read_data = file.read()
print(f"opened '{file.name}' from: '{os.getcwd()}'")

# readline() - reads one line and moves the marker further to newone
# readlines() - makes the list of lines
# read() - makes one blob/string object
# write('teeext') - writes + returns the number of chars written // len(text)
#
# tell() - return current position as number of read bytes
# seek(offset, from where) - change the current position

##################### 3. JSON #####################
import json
mylist = [3.14, 'adam', 'stas']
print(f'json reading: {json.dumps(mylist)}')
json.dump(mylist, open('../output.json', 'w'))
# .dumps -> return string
# .dump -> put to a file
# .loads -> load a string
# .load -> load a file