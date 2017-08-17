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

    # call function and pass object >> this is polymorphism, the function doesn't know what
    in_the_forest(donald)
    in_the_pond(fido)
    '''/
The duck cannot bark
The duck has feathers
The dog cannot quack
Walks like a dog'''

def in_the_forest(doggo): #object parameter with function
    doggo.bark()
    doggo.fur()

def in_the_pond(ducko): # object parameter with function
    ducko.quack()
    ducko.walk()


if __name__ == "__main__": main()
