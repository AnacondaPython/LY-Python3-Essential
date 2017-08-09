#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # <class 'int'> 42
    num = 42 
    print(type(num), num)
    
    # <class 'float'> 42.0
    num = 42.0
    print(type(num), num)

    # <class 'float'> 4.666666666666667
    num = 42 /9
    print(type(num), num)

    # <class 'int'> 4
    num = 42//9
    print(type(num), num)

    # Line split
    print("-----------------")

    # <class 'float'> 4.67 , 2 digit signifant figures
    num = round(42/9,2)
    print(type(num), num)

    # <class 'int'> 6
    num = 42 % 9
    print(type(num), num)

    # <class 'int'> 42, float to int
    num = int (42.9)
    print(type(num), num)

    # <class 'float'> 42.0, int to float
    num = float(42)
    print(type(num), num)


if __name__ == "__main__": main()
