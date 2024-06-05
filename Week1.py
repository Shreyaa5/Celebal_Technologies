def lower_triangular(n):
    for i in range(1, n + 1):
        print('* ' * i)
n = 5
lower_triangular(n)


def upper_triangular(n):
    for i in range(n, 0, -1):
        print('* ' * i)
n = 5
upper_triangular(n)


def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
n = 5
pyramid(n)





