#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "lines.txt")
outlines = os.path.join(dir_path, "new.txt")

def main():
    infile = open(lines)
    outfile = open(outlines, 'w')
    for line in infile:
        print(line, file = outfile, end= '')
    print('Done.')

if __name__ == "__main__": main()
