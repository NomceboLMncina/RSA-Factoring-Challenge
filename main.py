#!/usr/bin/python3
def check_factor(my_list):
    """check factor of number in a list"""
    if len(my_list) == 0 or my_list is None:
        print("An error occured")
    for q in my_list:
       l = int(a)
       for m in range(2,100):
           if l % m == 0:
               print("{:d}={:d}*{:d}".format(l, int(l/m), m))
               break
def factoring_challenge():
    """factor two numbers"""
    import sys

    with open(sys.argv[1]) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        print("Length: {:d}".format(len(lines)))
    check_factor(lines)
factoring_challenge()
