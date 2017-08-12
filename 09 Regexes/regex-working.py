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
This I whispered, and an echo murmured back the word, "Lenore!"
Quoth the raven, "Nevermore."
''' # print out whole sentences
    fh = open(lines)
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')


    '''/
Lenore
Lenore
Lenore
Lenore
Nevermore
Nevermore
''' # Print out each word only
    fh = open(lines)
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            match = re.search('(Len|Neverm)ore', line)
            if match:
                print(match.group())


if __name__ == "__main__": main()
