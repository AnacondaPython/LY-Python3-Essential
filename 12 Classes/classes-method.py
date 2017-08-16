#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    #constructor, used to initialize values when obj created
    def __init__(self, value=4):
        self._v = value #attribute / prop of object, can use in methods
        print('constructor')

    def quack(self): #self is reference to object, not class
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    '''/
constructor
Quaaack! 52
Walks like a duck. 52'''
    donald = Duck(52)
    donald.quack() #method  donald.quack(donald) gets passed automatically, hence "self"
    donald.walk() #method

    '''/
constructor
Quaaack! 4
Walks like a duck. 4'''
    frank = Duck() # must pass a value or have it initialized in constructor
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()
