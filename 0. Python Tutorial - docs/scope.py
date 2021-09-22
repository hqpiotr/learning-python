"""
Python Tutorial: https://docs.python.org/3/tutorial/classes.html
Scopes
"""

# 1. Scope local global nonlocal
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    do_local()
    print("After local assignment:", spam) # After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam) # After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam) # After global assignment: nonlocal spam

scope_test()
print("In global scope:", spam) # In global scope: global spam

