#Program to check if a number is a Fibonacci number
import os
import sys
from math import sqrt

def isSquare(x):
    s = int(sqrt(x))
    return s*s == x

def isFibonacci(n):
    if isSquare(5*n*n - 4) or isSquare(5*n*n + 4):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    print(isFibonacci(x))

    
