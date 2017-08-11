#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line,end='')

if __name__ == "__main__":
    import os

    curr_dir = 'c:\\www\\Ex_Files_Python_3_EssT(1)\\Ex_Files_Python_3_EssT\\Exercise Files\\07 Loops'
    os.chdir(curr_dir)
    main()