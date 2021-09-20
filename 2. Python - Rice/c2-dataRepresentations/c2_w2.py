# lists

"""
    pop (index) // remove from the index, default last = -1)
    remove('rabbit') // remove the element where value=
    append(x) // at the end, if list - put a list o flists
    .extend(smallerlist_to_be_added) // put values only, merge
    .insert(index, val) // particular index and val
    .copy (make a 2nd item) // reference ommitting problems
    .clear()
    list.reverse // in list changes the vals, returns nothing
    reversed(list) // return list, original not changed
    .sort(key lambda, reverse=true) // write predicate for key
"""

l = list(range(0, 100, 10))
print(l)

print("\n")
my_list = [1, 3, 5, 7, 9]
x = my_list.reverse()
print(my_list.reverse())
print(x)

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()


# updated list
print('Updated List:', systems)