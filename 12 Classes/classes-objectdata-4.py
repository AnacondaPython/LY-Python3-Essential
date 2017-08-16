#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # kwargs dictionary style approach is better for data control
    # generic variable methods are more powerful
    # lots of versatility with data, common template in python
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # Any attribute name
    def set_variables(self, k, v):
        self.variables[k] = v
    
    # Any attribute name
    def get_variables(self ,k):
        return self.variables.get(k,None)

def main():
    hobo = Duck(feet=2)
    hobo.set_variables('color', 'blue')
    print(hobo.get_variables('feet')) # 2
    print(hobo.get_variables('color')) # blue

if __name__ == "__main__": main()
