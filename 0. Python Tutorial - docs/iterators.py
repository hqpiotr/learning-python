# Each object has iterator to move from iter to next.
# Iterators, generators, yield
s = "abecadlo"
it = iter(s)

print(it)
print(next(it))
print(next(it))
print(next(it))
print("\n")

class Animal:
    def __init__(self, p_name, direction='fwd'):
        self.name = p_name
        self.direction = direction

        if direction == 'fwd':
            self.index = -1
        else:
            self.index = len(self.name)

    def __iter__(self):
        return self

    def __next__(self):
        print('using next')
        if self.index == len(self.name) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.name[self.index]

    # def __reversed__(self):
    #     print('using reversed')
    #     if self.index == 0:
    #         raise StopIteration
    #     else:
    #         self.index -= 1
    #     return self.name[self.index]


    def introduce(self):
        print(self.name)

a = Animal("horse", direction='fwd')
a.introduce()

for letter in a:
    print(f'{letter}', end=' ')
print("\n")

# b = Animal("dog", direction='rev')
# b.introduce()

# REVERSED, yield: generator to create iterator
# yeld creates __iter__ and __next__ automatically. but where?
def rev(input):
    for i in range(len(input)-1, -1, -1):
        yield input[i] # TODO: here!!!!!!!!!!!!!!!!!!
def rev_v2(input):
    for i in range(len(input)-1, -1, -1):
        print(input[i])

rev_v2('spam')
for char in rev('golf'):
    print(char)


# automated tests being run... awesom
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests