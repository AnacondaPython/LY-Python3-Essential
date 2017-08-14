#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

'''/0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 '''
def main():
    for n in testfunc(): print(n, end= ' ')

# can return any object you want really
def testfunc():
    return range(25)

if __name__ == "__main__": main()
