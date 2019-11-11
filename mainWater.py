#Fill certain number of gallons of water into a jug from two others
import os
import sys
from math import gcd

def isPossible(a,b,c):
    if c%gcd(a,b) == 0 and c<=max(a,b):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    isPossible(5,3,4)
    
