#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    
    def bark(self):
        print('The duck cannot bark')
    
    def fur(self):
        print('The duck has feathers')

class Dog:
    def bark(self):
        print('Woof!')
    
    def fur(self):
        print('The dog has brown and white fur')
    
    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')

def main():
    donald = Duck()
    fido = Dog()

    for o in (donald,fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

    '''/
Quaaack!
Walks like a duck.
The duck cannot bark
The duck has feathers
The dog cannot quack
Walks like a dog
Woof!
The dog has brown and white fur'''



if __name__ == "__main__": main()
