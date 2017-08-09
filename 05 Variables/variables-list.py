#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    '''/ <class 'tuple'> (1, 2, 3) '''
    # tuple are immutable, cannot change. Tuples use ()
    x = (1, 2, 3)
    # x.append(5) >> not allowed
    print(type(x),x)

    '''/ <class 'list'> [1, 2, 7, 3, 5] '''
    # list are mutable, can change. Lists use []
    y = [1,2,3]
    y.append(5)
    y.insert(2,7)
    print(type(y),y)

    '''/ <class 'str'> ri '''
    # s[0] t[1] r[2] i[3] n[4] , the last value is not included
    z = 'string'
    print(type(z),z[2:4])

    '''/ prints 1,2,3,4,5 each line'''
    a = (1,2,3,4,5)
    for i in a:
        print(i)

    '''/ prints s,t,r,i,n,g each line'''
    b = 'string'
    for i in b:
        print(i)



if __name__ == "__main__": main()
