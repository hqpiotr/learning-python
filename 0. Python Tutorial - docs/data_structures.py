# s1 = "oainerrjldawe5flj"
# s2 = "oaisnd6oanwfoienfo"
s1 = 'zabc 123'
s2 = 'xabc 193'

same_letters = [x for x in s1 for y in s2 if x==y]
print("same_letters", same_letters)

diff_letters = [(x,y) for x in s1 if x not in s2 for y in s2 if y not in s1]
diff_letters = sorted(set(diff_letters))
print("diff_letters", diff_letters)

# Make a tuple of diff chars from same indexes places in string (zip)
tup_diff = [(x,y) for x,y in zip(s1, s2) if x not in s2 and y not in s1]
print("tup_diff", tup_diff)
# --> (z, x), (2, 9)

# Excercise: print a tuple elements only
for row in tup_diff:
    for val in row:
        print(val)

# Make a list from tuples using list_comprehension
list_diff = [value for row in tup_diff for value in row]
print("list_diff", list_diff)
# --> [z, x, 2, 9]

for i in enumerate(list_diff):
    print(i)

for i, v in enumerate(list_diff):
    print(v)

# SET - this is a list without duplicates. not sorted by automate
# created as dict with one values only
myset = {'abc', 'zoo', 'one', 'two', 'one', 'two', 'three', 'zee'}
print("myset", sorted(myset))