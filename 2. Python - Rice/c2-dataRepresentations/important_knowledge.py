# list comprehension with condition if else:
    output_list = [x+1 if x >= 45 else x+5 for x in input_list]

# return longer string:
    max(string_1, string_2, key=len)
    min(string_1, string_2, key=len)

# enumerate elements in lists to get the index (print tuples):
    for element in enumerate(list):
        print(element)
        """
            ('0', 'eat')
            ('1', 'sleep')
            ('0', 'repeat')
        """

# enumerate elements in list, but print separately
  for index, element in enumerate(list):
        print(index, "\t", element)
        """
            0     eat
            1     sleep
            0     repeat
        """

# find string difference
  [i for i in range(len(string1) if string1[i] != string2[i])]
      # example: [a, x, 4]
