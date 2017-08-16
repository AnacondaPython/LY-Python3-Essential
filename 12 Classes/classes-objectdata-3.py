#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # kwargs dictionary style approach is better for data control
    # generic variable name more versatile + scalable
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # reference generic vars
    def set_color(self, color):
        self.variables['color'] = color 
    
    # reference generic vars
    def get_color(self):
        return self.variables.get('color', None)

def main():
    foo = Duck(color = 'blue')
    print(foo.get_color()) # blue

    bar = Duck()
    print(bar.get_color()) # None

    hobo = Duck(feet="2") # can pass w/e you want

if __name__ == "__main__": main()
