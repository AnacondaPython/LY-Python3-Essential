#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    func()
    func2(2)
    func3()
    func3(5)

# def means function
def func():
    for i in range(10):
        print(i, end = ' ')
    print()

# pass arguments to function
def func2(a):
    for i in range (a,10):
        print(i, end = ' ')
    print()

# default value parameter
def func3(a=7):
    for i in range (a,10):
        print(i, end = '')
    print()


if __name__ == "__main__": main()
