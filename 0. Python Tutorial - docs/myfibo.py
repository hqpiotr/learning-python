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
