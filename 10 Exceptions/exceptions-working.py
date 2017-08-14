#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "xlines.txt")

def main():
    try:
        fh = open(lines)
    except IOError as e: #specifying "IOerror as e" not needed can use a catchall
        print('could not open the file. come back tomorrow',e)
    else:
        for line in fh: print(line.strip())

    
    # Alternate method no "else"
    try:
        fh = open(lines)
        for line in fh: print(line.strip())
    except IOError as e: 
        print('could not open the file. come back tomorrow',e)
if __name__ == "__main__": main()
