#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the basic generator file.")
    '''/0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 /n'''
    # prints  0 to 24
    for i in range(25):
        print(i, end = ' ')

    '''/0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 /n'''
    # Prints 0 to 25
    for i in inclusive_range(0,25,1):
        print(i,end= ' ')

# Generator by itself
def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()


