#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the advanced generator file.")
    # Advanced error check version, can specify 1 to 3 args

    # 0 to 25
    '''/0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 /n'''
    for i in inclusive_range_advanced(25):
        print(i, end = ' ')
    
    # 5 to 25
    '''/5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 /n'''
    for i in inclusive_range_advanced(5,25):
        print(i, end = ' ')

    # 5 to 23, every 3rd value
    '''/5 8 11 14 17 20 23 /n'''
    for i in inclusive_range_advanced(5,25,3):
        print(i, end = ' ')

    # catch errors if 4 args
    '''/inclusive_range expected at most 3 arguments, got 4'''
    #for i in inclusive_range_advanced(5,25,3,4):
    #    print(i, end = ' ')

def inclusive_range_advanced(*args):
    # error checks for num of arguments
    numargs = len(args)
    if numargs < 1 : raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step =1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    
    # generator portion
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__": main()