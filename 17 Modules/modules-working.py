#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))  # Python version 3.6.2
    print(sys.platform) # win32 , not actual OS, use importOS

    #allows you to selectively import
    import os
    print(os.name) # nt
    print(os.getenv('PATH')) # full path spans 5 lines, boxcryptor, java, python 36, nodeJS, microsoft VScode, NPM
    print(os.getcwd()) # c:\www\Ex_Files_Python_3_EssT(1)\Ex_Files_Python_3_EssT\Exercise Files   , this is currentworking directory
    print(os.urandom(25)) # string of random bytes, >> b"e\xcb\x19\xaa\xf7l4\xfb'\xe5\xe2\xe5w\xaf$'M\x8d\xa5\x1ec\xb8Qk\x1c"

    # -------------------------------------
    # import urllib.request
    # page = urllib.request.urlopen('http://bw.org/') # cannot open, certificate verify failed, supposed to grab HTML of webpage
    # for line in page: print(str(line, encoding = 'utf_8'), end= '')
    # -------------------------------------

    # shuffle up elements in the array
    import random
    print(random.randint(1,1000)) #578
    x = list(range(25))
    print(x) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    random.shuffle(x)  
    print(x) # [14, 16, 7, 1, 8, 17, 6, 2, 22, 19, 18, 3, 9, 13, 20, 21, 11, 5, 23, 12, 10, 4, 15, 0, 24]
    random.shuffle(x)
    print(x) # [17, 24, 18, 3, 14, 20, 16, 12, 10, 23, 9, 13, 1, 15, 4, 7, 6, 11, 2, 8, 22, 19, 5, 0, 21]

    import datetime
    now=datetime.datetime.now()
    print(now) # 2017-08-19 11:29:48.477473
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) # 2017 8 19 11 29 48 477473

if __name__ == "__main__": main()
