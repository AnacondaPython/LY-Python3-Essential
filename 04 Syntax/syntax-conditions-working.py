#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 0,1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is not less than b")
    else:
        print("a is equal to b")

#private a,b values
def other():
    a, b = 1,1 
    s = "less than" if a < b else "not less than" #ternary operator "a if condition else b"
    print(s)

if __name__ == "__main__": main()
other() #call stack