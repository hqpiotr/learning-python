# Make a list_of_lists of dicts
import  random

rows = 5
cols = 5
list_of_lists = []
list_of_dicts = []
dict_of_lists = {}
dict_of_dicts = {}
NAMES = ("piotr", "ola", "bartus", "stas", "nel")
JOBS = ("engineer", "manager", "director")

def create_list_of_lists(nr, nc):
    for r in range(nr):
        internal_list = []
        for c in range(nc):
            internal_list.append(random.randrange(0,9,1))
        list_of_lists.append(internal_list)

def create_list_of_dicts(nr, nc):
    for r in range(nr):
        nested_dict = {}
        for c in range(nc):
            nested_dict[NAMES[c]] = nested_dict.get(NAMES[c],
                                                    random.randrange(0,9,1))
        list_of_dicts.append(nested_dict)

def create_dict_of_lists(nr, nc):
    for i in range(nr):
        nested_list = []
        for c in range(nc):
            nested_list.append(random.randrange(0,9,1))
        dict_of_lists[NAMES[i]] = dict_of_lists.get(NAMES[i], nested_list)

def create_dict_of_dicts(nr, nc):
    for i in range(nr):
        nested_dict = {}
        for j in range(nc):
            nested_dict[NAMES[j]] = nested_dict.get(NAMES[j],
                                                    random.randrange(0,9,1))

        dict_of_dicts[JOBS[i]] = dict_of_dicts.get(JOBS[i], nested_dict)

def print_dict_of_dicts(table):
    print("\n{")

    for k in table.keys():
        print("\t\t" + k + ":")
        for v in table.values():
            print("\t\t\t" + str(v), end=' ')
            print()

    print("}")


def print_dict_of_lists(table):
    for k in table:
        print("[" + k + "]: ", table[k], end='\n')

def print_list_of_lists(table):
    for i in table:
        print(i)

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
""" 1 """
create_list_of_lists(3, 3)
print(list_of_lists, "\n")
print_list_of_lists(list_of_lists)
print()
""" 2 """
create_list_of_dicts(3, 3)
print(list_of_dicts, "\n")
print_list_of_dicts_v1(list_of_dicts)
print_list_of_dicts_v2(list_of_dicts)
print(list_of_dicts.pop())
""" 3 """
create_dict_of_lists(3,3)
print(dict_of_lists, "\n")
print_dict_of_lists(dict_of_lists)
""" 4 """
create_dict_of_dicts(3,3)
print(dict_of_dicts)
print_dict_of_dicts(dict_of_dicts)
print(dict_of_dicts['director']['bartus'])