##################### 3. JSON #####################
import json
mylist = [3.14, 'adam', 'stas']
print(f'json reading: {json.dumps(mylist)}')
json.dump(mylist, open('../output.json', 'w'))
# .dumps -> return string
# .dump -> put to a file
# .loads -> load a string
# .load -> load a file