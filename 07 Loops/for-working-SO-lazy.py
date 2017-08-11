#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "lines.txt")
# open(lines)
# ...

def main():
    fh = open(lines)
    for line in fh.readlines():
        print(line, end='')

if __name__ == "__main__": main()