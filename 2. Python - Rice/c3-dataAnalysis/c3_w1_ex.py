"""
Write a function count_letters(word_list) that takes as input a list of words that
are composed entirely of lower case letters . This function should return the lower
case letter that appears most frequently (total number of occurrences) in the words
in word_list. (In the case of ties, return the earliest letter in alphabetical order.)

The Python code snippet below represents a start at implementing count_letters using
a dictionary letter_count whose keys are the lower case letters and whose values are
the corresponding number of occurrences of each letter in the strings in word_list..
"""

def count_letters(word_list):
    chars = {}
    word_list = word_list.replace(" ", "")

    for char in word_list:
        chars[char] = chars.get(char, 0) + 1

    reversed_chars = {}
    for k, v in chars.items():
        reversed_chars[v] = reversed_chars.get(v, k)

    for item in sorted(reversed_chars, reverse=True):
        print(reversed_chars[item] + ": #" + str(item))
        break


# my_string = "isten strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
# count_letters(my_string)

