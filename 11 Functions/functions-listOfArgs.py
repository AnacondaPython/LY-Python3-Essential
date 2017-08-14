#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1,2,3,42,43,45,56)

def testfunc(ed, edd, eddy, *args):
    print(ed, edd, eddy, args)  #1 2 3 (42, 43, 45, 56) tuple
    print(ed, edd, eddy, *args) # 1 2 3 42 43 45 56  (value at address)
    for n in args:print (n, end=' ')

if __name__ == "__main__": main()
