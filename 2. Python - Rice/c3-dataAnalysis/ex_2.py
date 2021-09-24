# Make a list_of_lists of dicts
import  random

rows = 5
cols = 5
list_of_lists = []
list_of_dicts = []
NAMES = ("piotr", "ola", "bartus", "stas", "nel")

def create_list_of_lists(nr, nc):
    for r in range(nr):
        internal_list = []
        for c in range(nc):
            internal_list.append(random.randrange(0,9,1))
        list_of_lists.append(internal_list)

def print_list_of_lists(table):
    for i in table:
        print(i)

def create_list_of_dicts(nr, nc):
    for r in range(nr):
        nested_dict = {}
        for c in range(nc):
            nested_dict[NAMES[c]] = nested_dict.get(NAMES[c],
                                                    random.randrange(5,9,1))
        list_of_dicts.append(nested_dict)

def print_list_of_dicts_v1(table):
    for i in table:
        print(i)
    print()

def print_list_of_dicts_v2(table):
    for e, i in enumerate(table):
        print("row[" + str(e) + "]\t", end='')
        for k, v in i.items():
            print('"' + str(k) + '": ' + str(v), end='\t')
        print("")


""" testing """
create_list_of_lists(3, 3)
print(list_of_lists, "\n")
print_list_of_lists(list_of_lists)
print()
create_list_of_dicts(3, 3)
print(list_of_dicts, "\n")
print_list_of_dicts_v1(list_of_dicts)

# tell me what has piotr is second row
# print(list_of_dicts[2]['bartus'])
print_list_of_dicts_v2(list_of_dicts)
print(list_of_dicts.pop())
