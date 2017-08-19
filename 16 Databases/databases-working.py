#!/usr/bin/python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def main():
    # connects db, creates file if no exist
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one',1)) # t1 is text field. i1 is a number field. They are arbitrarily named
    db.execute('insert into test (t1, i1) values (?, ?)', ('two',2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('seven',7))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three',3))
    db.commit()  # commit changes
    '''/
    ('one', 1)
    ('seven', 7)
    ('three', 3)
    ('two', 2)''' #sort by alphabetical "text" order
    cursor = db.execute('select * from test order by t1') 
    for row in cursor:
        print(row) #data comes in tuple form

    '''/
    (1, 'one')
    (7, 'seven')
    (3, 'three')
    (2, 'two')''' #sort by alphabetical "text" order, but swap text / number positions
    cursor = db.execute('select i1, t1 from test order by t1') 
    for row in cursor:
        print(row) #data comes in tuple form

    '''/
    (1, 'one')
    (2, 'two')
    (3, 'three')
    (7, 'seven')''' #sort my number A-Z alphanumeric
    cursor = db.execute('select i1, t1 from test order by i1') 
    for row in cursor:
        print(row) #data comes in tuple form

if __name__ == "__main__": main()
