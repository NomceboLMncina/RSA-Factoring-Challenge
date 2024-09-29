#!/usr/bin/python3
def is_prime(number):
    """Check if a number is prime
    using primilarity test"""
    import math
    l = 2
    while (l <= math.sqrt(number)):
        if (number % l == 0):
            return False
        l += 1
    return (True)
#print(is_prime(19))
#print(is_prime(21))
