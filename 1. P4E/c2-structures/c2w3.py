# 3. lists and dictionaries and tuples

def lists_fun():
    l1 = ['a', 3.0, 'string', [1, 1], 0]
    for element in l1:
        print('element:', element)

    l2 = list()
    l2.append(1)
    l2.append(2)
    l2.append(3)
    print("new list initiated from scratch:")
    print(l2[0:len(l2)])
    l2.sort()
    # len, min, max, sort,
    # split - breaks a string with spaces: string = "Three new words"; string.split(\delimeter;)


def dictionaries_fun():
    #like hashmap, memory based key: value stores.
    d1 = dict() # or d1 = {}
    d1['laptop'] = 2.0
    d1['pecet'] = 10.0
    print(d1)
    # shows { 'laptop' : 2.0, 'pecete': 10.0 }

    d2 = {'apple' : 1, 'banana' : 2.0, 'citron' : 3.3 }
    print(d2)

    # check if something exists: if KEY in DICT
    # or use get method: dict.get(KEY/word, DEFAULT_COUNT_IF_NOT_EXISTING=0)
    # print each pair:     # for key in dictionary:     # print(key, dictionary[key])
    list1 = d2.keys()
    print(list1)
    list2 = d2.values()
    print(list2)

    sth = d2.items() # tuples
    print(sth)

    for i, j in d2.items():
        print (i, j)


def dictionary_exercise(handle):
    # Who sent the biggest amount of mails - return mail + number
    map = dict() # or map = {}
    for line in handle:
        if not line.startswith('From '):
            continue
        else:
            words = line.split()
            name = words[1]
            map[name] = map.get(name, 0) + 1

    maxcount, maxkey, maxvalue = 0, 0, 0
    for map_key, map_value in map.items():
        if maxcount < map_value:
            maxcount = map_value
            maxkey = map_key
            maxvalue = map_value

    print(maxkey, maxvalue)
    #print(map[maxkey])


def check_tuples():
    t1 = tuple()
    t2 = (2, 3, 4)
    print (t1, t2)

def list_comprehension_IMPORTANT():
    slownik = {'a': 8, 'b': 5, 'c': 3}
    print(sorted([(v, k) for k, v in slownik.items()]))

    '''
        alternatively instead of above, do it in snippet
    '''
    l = list()
    for k, v in slownik.items():
        newtuple = (v, k)
        l.append(newtuple)
    l = sorted(l)
    print(l)

    l2 = list()
    l2 = sorted([v, k] for k,v in slownik.items())
    print(l2)

    l3 = [4, 7, 1, 3, 2]
    l3 = sorted(l3)
    print(l3)


if __name__ == "__main__":
    lists_fun()
    dictionaries_fun()
    check_tuples()
    list_comprehension_IMPORTANT()
    filename = "input_spammers.txt"
    dictionary_exercise(filename)

