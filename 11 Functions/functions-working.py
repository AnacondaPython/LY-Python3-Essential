#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc()
    testNum(42, 34, 75) #43, 34, 75 output
    testNumOptional(42) # 42, 112, 66
    testNumOptional(42,45) #42, 45, 66

def testfunc():
    pass #No-operation ,noop

def testNum(number, another, onemore): #must pass 3 arguments
    print('This is a test function', number, another, onemore)

def testNumOptional(number, another=None, onemore =66): #To make arguments optional, explicitly define initial value. "None" works as well
    if another is None:
        another = 112
    print('This is a test function', number, another , onemore)

if __name__ == "__main__": main()
