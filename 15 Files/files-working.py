#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "lines.txt")

def main():
    f = open(lines ,'r') #r is default, for read.  `r+` is read/write. `rb` is read binary. `w` is write
    for line in f.readlines(): #or just f instead of f.readlines()
        print(line, end = '')

if __name__ == "__main__": main()
