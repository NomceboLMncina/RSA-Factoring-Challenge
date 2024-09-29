#!/usr/bin/python3
def is_sqr(number):
    """check if a number is squared"""
    import math

    x = int(math.sqrt(number))
    if (x * x == number):
        return (True)
    return (False)
def is_rsa(n):
    """split the rsa of a number"""
    import math
    from prime import is_prime

    x = int(math.sqrt(n)) + 1
    while True:
        y = x ** 2 - n
        if is_sqr(y):
            z = math.sqrt(y)
            break
        x = x + 1
    print(is_prime(x + z))
    print(is_prime(x - z))
    print("{:d}={:d}*{:d}".format(int(n), int(x + z), int(x - z)))
is_rsa(35)
