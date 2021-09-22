def print_fib(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib(n):
    a, b = 0, 1
    res = []
    while a <= n:
        res.append(a)
        a, b = b, a + b
    print(res)


# execute this every time myfibo is executed from command

# for testing purposes, e.g. >>>> python myfibo.py 9
#                                 0 1 1 2 3 5 8
if __name__ == "__main__":
    import sys

    print(dir(sys))
#    fib(int(sys.argv[1]))
