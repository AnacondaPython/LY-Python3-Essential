#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, 'olives.jpg')
outlines = os.path.join(dir_path, 'new.jpg')

def main():
    buffersize = 50000
    infile = open(lines, 'rb')
    outfile = open(outlines, 'wb')
    buffer = infile.read(buffersize)

    # Creates an image by reading old "olives.jpg" binary into "new.jpg"
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done.')

if __name__ == "__main__": main()