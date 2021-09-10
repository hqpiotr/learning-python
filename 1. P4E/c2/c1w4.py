# load input file and check how many e-mails users send, and select the spammer.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


def read_users(filename):
    try:
        handle = open(filename, 'r')
    except:
        print('no such file exists')
        quit()

    map = dict()
    # or map = {}

    for line in handle:
        if not line.startswith('From '):
            continue
        else:
            startname = line.find(' ')
            endname = line.find('@')
            fullname = line[startname+1:endname]

            if '.' in fullname:
                # print('there was a . in name+surname')
                separator = fullname.find('.')
                firstname = fullname[:separator]
                lastname = fullname[separator+1:]
                user = firstname.capitalize() + " " + lastname.capitalize()
            else:
                user = fullname

        # put to the map, if doesn't exist (get checks that, put default value if not existing)
        map[user] = map.get(user, 0) + 1

        # alternatively: check if key is present, if not, put, if yes - overwrite
        # map[user] = somekey

    # show map
    for i, j in map.items():
        print(i,':', j)

    # find spammer
    biggest_spammer = ''
    biggest_emails = 0
    for i, j in map.items():
        if biggest_emails < j:
            biggest_emails = j
            biggest_spammer = i
        else:
            continue

    print('\nAnd the biggest spammer was:', biggest_spammer, 'with', biggest_emails, 'emails sent.')

"""
    Thorough explanation of the dicts from stackoverflow
        # create
            data = dict()
            data = {}
            
        # fill in
            data = {'a':1, 'b':2}
            data = dict(a=1,b=2)
            data = {k:v for k,v in ( ('a':1), ('b':2), ('c':3))}
            
        # update single value
            data['a'] = 4
            data.update({'a':4}]
            data.update(dict(a=4))
            data.update(a=1)
            
        # update multiple values
            data.update({'d':4, 'e':5})
            data |= {'d':4, 'e':5}
            
        # merge datas from dicts
            data3 = {}
            data3.update(data)
            
        # delete items
            del data[key] // remove element
            data.pop(key) // remove the key and return it's value
            data.clear() // empty all
            
        # create a dict from two lists
            data = dict(zip(list_with_keys, list_with_values))
"""

def example_list_comprehension():
    print("print(sorted( [ (k, v) for k, v in map.items() ])")



if __name__ == "__main__":
    filename = "input/input_spammers.txt"
    read_users(filename)
    mytuple = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    #print(mytuple[2])
    mylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    #print(mylist[0])
    print(sorted(mylist))
    #print(mylist)
