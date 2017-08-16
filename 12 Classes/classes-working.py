#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# duck is class, donald is object
# everything in python is an object, object oriented language
class Duck:
    # object method
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
