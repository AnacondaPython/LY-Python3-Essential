#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    '''\
one 1
two 2
three 3
four 4
five 5'''
    # normal way
    d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
    for k in d:
        print(k, d[k])

    # alternate way
    # sorted(d.keys()) not necessary anymore
    e = dict (
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    for k in e:
        print(k, d[k])


if __name__ == "__main__": main()
