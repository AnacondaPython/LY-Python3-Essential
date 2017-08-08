#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# class is definition when create object in python
class Egg:
    # constructor is function with __special name__
    # self is always first argument
    def __init__(self, kind = "fried"):
        self.kind = kind
    
    def whatKind(self):
        return self.kind

def main():
    # Create an object based on class using constructor __init__
    # self (python) and this (javascript) are same thing
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind())
    print(scrambled.whatKind())

if __name__ == "__main__": main()

# Definition, which is called class, defined blueprint of how objects made