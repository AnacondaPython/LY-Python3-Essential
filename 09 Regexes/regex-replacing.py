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
Tell this soul with sorrow laden if, within the distant Aidenn,
It shall clasp a sainted maiden whom the angels named ### -
Clasp a rare and radiant maiden, whom the angels named ###?"
Quoth the raven, "###."
''' # Items with matching desc have ### on it but output whole paragraph
    fh = open(lines)
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end='')

    '''/
Clasp a rare and radiant maiden, whom the angels named ###?"
Quoth the raven, "###."
''' # per line matching only
    fh = open(lines)
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')

if __name__ == "__main__": main()
