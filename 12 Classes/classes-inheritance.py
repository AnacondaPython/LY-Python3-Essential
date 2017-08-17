#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Virtually all classes like tuples and lists are inherited from common classes
class Animal:

    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin '' here !')
    def clothes(self): print('I have nice clothes')

class Duck(Animal): # Inherit Animal Class
    def quack(self):
        print('Quaaack!')
    
    def walk(self):
        super().walk() #use inherited method / properties from Animal
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
        print('I have brown and white fur')

def main():
    donald = Duck()
    donald.quack() #Quaaack!
    donald.walk() # Hey! Im walkin  here ! (Inherited from Animal) >> Walks like a Duck
    donald.clothes() # I have nice clothes

    fido = Dog() 
    fido.walk() # Hey I'm walking here! (Inherited from Animal)
    fido.clothes() # I have nice clothes

if __name__ == "__main__": main()
