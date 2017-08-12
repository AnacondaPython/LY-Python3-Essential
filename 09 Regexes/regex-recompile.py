#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "raven.txt")

def main():
    '''/
Quoth the raven, "Nevermore."
Quoth the raven, "Nevermore."
Shall be lifted - nevermore!
''' # Compile the regex one time at start, not per iteration anymore
    # include lowercase using re.IGNORECASE
    fh = open(lines)
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')
    '''/
Quoth the raven, "###."
Quoth the raven, "###."
Shall be lifted - ###!
''' # Can do pattern matching with sub
    fh = open(lines)
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end='')

if __name__ == "__main__": main()
