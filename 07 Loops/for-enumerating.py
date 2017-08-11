#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# initialize import
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "lines.txt")

def main():
    '''\
0 01 This is a line of text
1 02 This is a line of text
2 03 This is a line of text
3 04 This is a line of text
4 05 This is a line of text
''' # prev example
    fh = open(lines)
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')
    

    '''\
index 3 is an s
index 6 is an s
index 10 is an s
''' # for index, value in enumerate(iterator)
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's': print ('index {} is an s'.format(i))

    '''\
0 M
1 e
2  
3 s
4 t
5 r
6 i
7 n
8 g
''' # i is the index like 1,2,3,4,5
    # c is current char in 'Me string'
    for i, c in enumerate("Me string"):
        print (i,c)

if __name__ == "__main__": main()