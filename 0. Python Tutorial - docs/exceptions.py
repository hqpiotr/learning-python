"""
Python Tutorial: https://docs.python.org/3/tutorial/errors.html
Errors & Exceptions
"""

def myf(x, y):
    x/y

try:
    # raise ZeroDivisionError("text of an exc...")
    myf(4, 0)
# except BaseException as err:
#     print(f"Base! {err}")
except ZeroDivisionError as err:
    print(f"zero! {err}")
except TypeError as err:
    print(f"I won't reach this stage! {err}")
else:
    print('all went fine')
finally:
    print('\nCLEANING THIS MESS')


