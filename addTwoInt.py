#!/usr/bin/python3

import sys

def add(a, b):
    s = a + b
    return s

l=len(sys.argv)
if l == 3 :
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )

    print("Sum = ",add(a,b))

elif l == 1:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    print("Sum = ",add(a,b))
    
else:
    print("ERROR: Enter 2 values only")