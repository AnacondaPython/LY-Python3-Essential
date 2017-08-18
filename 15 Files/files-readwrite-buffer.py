#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "bigfile.txt")
outlines = os.path.join(dir_path, "new-big.txt")

def main():
    buffersize = 50000
    infile = open(lines)
    outfile = open(outlines, 'w')
    buffer = infile.read(buffersize)

# .......
# Done.
# has 7 dots, since 50,000 buffer in 320,000 bytes is 7 minimal
# Running this on the small file produces 1 dot
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done.')

if __name__ == "__main__": main()
