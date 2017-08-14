#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(one = 1, two = 2, four = 42)
    testfunc2(5,6,7,8,9,10, one = 1, two = 2, four = 42)
    testfunc3(5,6,7,8,9,10, one = 1, two = 2, four = 42)

# **Kwargs used as dict lookup
def testfunc(**kwargs): # keyword args  , conventional name only same as *args
    print('This is a test function', kwargs['one'],kwargs['two'], kwargs['four']) # This is a test function 1 2 42

# RESTRICTION in ORDER: Named arguments, arbitrary tuple args (*args), keyword args (**kwargs)
# Can have as many *args *arg1 *arg2 or **kwargs1 **kwargs2 **kwargs3 arguments as you want
def testfunc2(this, that, other, *args, **kwargs):
    print('This is a test function',
    this, that, other, args,
    kwargs['one'],kwargs['two'],kwargs['four'])



def testfunc3(this, that, other, *args, **kwargs):
    for k in kwargs: print(k, kwargs[k])
    for n in args: print(n)

if __name__ == "__main__": main()
