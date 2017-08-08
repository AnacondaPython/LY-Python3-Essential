#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a = "one"
    print("a is", a)
    print("a is type", type(a),a)
    
    b = "1"
    print("b is",b)
    print("b is type", type(b),b)

    c,d = 0,1
    print("c and d are", c,d)
    c,d = d,c
    print("c and d are", c,d)

    e = (1, 2, 3 ,4 ,5)
    print("e is tuple", e)
    f = [6, 7, 8 ,9 , 10]
    print("f is tuple", f)


if __name__ == "__main__": main()
