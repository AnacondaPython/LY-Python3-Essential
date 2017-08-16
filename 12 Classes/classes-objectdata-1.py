#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # good practice to give default value like color:white
    def __init__(self, color='white'):
        self._color = color

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    # No control over how property values changes
    donald = Duck()
    print(donald._color) # white
    donald._color = 'blue'
    print(donald._color) # blue

    # Better version to keep track of color changes (database-like schema)
    # encapsulation
    frank = Duck()
    print(frank.get_color()) #white
    donald.set_color('green')
    print(donald.get_color()) #green

if __name__ == "__main__": main()
