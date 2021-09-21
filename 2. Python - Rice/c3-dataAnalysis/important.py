md = {}
md['raz'] = 1
md = {'dwa': 2}
md['trzy'] = 3
md.update({'cztery': 7})
md.update(piec=10)
md['szesc'] = 0
for k in sorted(md.keys(), reverse=False):
    print(k)

for k in sorted( md.values()):
    print(k)

#new list
combos = [(x, y) for x in range(4) for y in range(4) if x != y]
print(combos)

#####
# TODO: important knowledge
#####
matrix = \
[
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
print("matrix:", matrix)
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
print("transposed:", transposed)
#### OR
new_from_comprehension = [[row[i] for row in matrix] for i in range(4)]
print("new_from_comprehension:", new_from_comprehension)

new_from_complexflox_upacking = list(zip(*matrix))
print("new_from_complexflox_upacking:", new_from_comprehension)


###
###
###
#TODO: To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
    What is your name?  It is lancelot.
    What is your quest?  It is the holy grail.
    What is your favorite color?  It is blue.
"""
string1 = "abcd efgh"
string2 = "abcd efXh"
for i, j in zip(string1, string2):
    print(i, j)

###
###
# TODO: loop thru unique elements in order.... sorted(set(x))...
# Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set()
# over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['grapes', 'ziziku', 'apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
"""
apple
banana
orange
pear
"""



s1 = "oainerfjldawenflj"
s2 = "oaisndoanwfoienfo"

same_letters = [x for x in s1 for y in s2 if x==y]
print("\n", sorted(set(same_letters)))
