#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # this is true
    a, b = 0 ,1
    if a < b:
        print('this is true')
    else:
        print('it is not true')
    
    # this is true
    if True:
        print('this is true')
    else:
        print('it is not true')

    # is it not true
    if False:
        print('this is true')
    else:
        print('it is not true')

if __name__ == "__main__": main()
