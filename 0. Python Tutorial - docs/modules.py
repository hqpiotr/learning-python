# Modules
# print(x, end='') --> changes the delimter from \n!
import myfibo
from myfibo import print_fib
from myfibo import fib as fibonacci



myfibo.print_fib(5)
print_fib(10)
fibonacci(15)

y = myfibo
useful = [x for x in dir(y) if not x.startswith("__") if not x.endswith(
    "__")]
print(useful)

# print(fibo_var) error
print(myfibo.fibo_var)
# Packages
"""
To be able to use . dotted line calling: myfibo.fib
They do not care about each others namespaces.

__init__.py is required to treat directories as packages.
// can be empty...

Collection of modules is called a package. Structure:
sound/
    __init__.py
    formats/
        __init__.py
        wav.py
        mp3.py
        ...
    effects/
        __init__.py
        echo.py
        surrond.py

Users can import modules from packages individually:
>>> import sound.effects.echo
then reference sound.effects.echo.doSth(a,b,c)
... or
>>>> from sound.effects import echo
echo.do_sth_else(x)
"""
