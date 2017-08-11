#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #initlaize
    s = 'this is a string'

    '''\ this is a string'''
    for c in s:
        print(c, end='')
    
    '''\ thi i a tring'''
    for c in s:
        if c == 's': continue #ignore c
        print(c,end='')
    
    '''\ thi'''
    for c in s:
        if c == 's': break #stop at first c
        print(c,end='')
    
    # ---------------------------
    # You can have else sattements in `for` or `while` to trigger once break conditions met
    # other programming languages don't do this
    # ---------------------------

    '''\ this is a stringelse'''
    for c in s:
        print(c, end='')
    else:
        print('else')
    
    '''\ this is a stringelse'''
    i = 0
    while (i < len(s)):
        print(s[i],end='')
        i+=1
    else:
        print('else')
    
if __name__ == "__main__": main()
