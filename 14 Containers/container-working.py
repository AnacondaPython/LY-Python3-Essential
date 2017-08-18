#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "utf8.txt")

def main():
    #fin means "file in" its a variable
    fin = open( lines, 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            # integer equivalent of char ASCII
            if ord(c) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(c)),encoding ='utf_8') # addition operator on mutable container type
            else: outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file=fout)
    print(outstr)
    print('Done')

'''/
This is a UTF-8 file. 
It has some interesting characters in it. 
&#1641;(&#0865;&#3663;&#0815;&#0865;&#3663;)&#1782;   

Done
''' #UTF-8 format ٩(͡๏̯͡๏)۶ each character



if __name__ == "__main__": main()
