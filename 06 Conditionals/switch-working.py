#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict (
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )

    # "three"
    v = 'three'
    print (choices[v])

    # "other" >> as 'seven' has no matching dict key
    x = 'seven'
    print (choices.get(x, 'other'))

if __name__ == "__main__": main()
