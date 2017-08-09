#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # This is a    >> newline
    # string!
    s = "This is a \nstring!"
    print(s)

    # This is a \nstring!     >> raw strings to print newline inclusive using "r"
    s = r"This is a \nstring!"
    print(s)

    # This is a 42 string!  >>  python 3 way
    n = 42
    s ="This is a {} string!".format(n)
    print(s)

    # This is a 42 string!  >>  old way in python 2, to be deprecated
    n = 42
    s = "This is a %s string!" % n
    print(s)

    # This is a string   >> multiline print
    # line after line
    # of text and more
    n = 42
    s = '''\
this is a string
line after line
of text and more
    '''
    print(s)

if __name__ == "__main__": main()
