#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # kwargs dictionary style approach is better for data control
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    foo = Duck(color = 'blue')
    print(foo.get_color()) # blue

    bar = Duck()
    print(bar.get_color()) # white

    hobo = Duck(feet="2") # can pass whatever you want

if __name__ == "__main__": main()
