#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    '''/ this is true'''
    # simple expanded conditional statement
    a,b = 0,1
    if a < b:
        v = 'this is true'
    else:
        v = 'this is not true'
    print(v)

    '''/ a is smaller than b'''
    # ternary operator
    # [true] if (condition) else [false]
    x = 'a is smaller than b' if a < b else 'a is greater than or equal'
    print(x)

if __name__ == "__main__": main()
