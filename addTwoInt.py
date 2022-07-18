#!/usr/bin/python3

import sys

def add(a, b):
    s = a + b
    return s


a = int( sys.argv[1] )
b = int( sys.argv[2] )

print(add(a,b))