#!/usr/bin/env python3

import sys
from sympy import factorint

def factor_rsa_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                if number <= 1:
                    print(f"{number} is not a valid RSA number.")
                    continue
                
                factors = factorint(number)
                factors_str = ' * '.join([f"{prime}^{exponent}" for prime, exponent in factors.items()])
                print(f"{number} = {factors_str}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Ensure all lines in the file contain valid integers.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa.py <file>")
        sys.exit(1)
    
    factor_rsa_numbers(sys.argv[1])
