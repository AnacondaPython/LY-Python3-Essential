#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class inclusive_range:
    def __init__(self, *args): # define attributes init
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs ==1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = arg
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self): #makes object iteratable when created
        i = self.start
        while i <= self.stop:
            yield i #makes this a generator
            i += self.step

def main():

    '''/5 7 9 11 13 15 17 19 21 23 /n'''
    # regular range function builtin
    o = range(5,25, 2)
    for i in o: print(i, end = ' ')

    print('/n')

    '''/5 7 9 11 13 15 17 19 21 23 25'''
    #Custom made class
    o = inclusive_range(5,25,2)
    for i in o: print(i, end = ' ')
    # for i in o.iter(): print(i, end = ' ')  # iter is not needed because we defined that in class
    # can be used in database app, parsing files

if __name__ == "__main__": main()
