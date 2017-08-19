#!/usr/bin/python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

#database driver all selfcontained, fully capable
def main():
    # connects db, creates file if no exist
    db = sqlite3.connect('test2.db') 
    db.row_factory = sqlite3.Row  # add this line to change for row returned from cursor based on built-in row factory provided
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one',1)) # t1 is text field. i1 is a number field. They are arbitrarily named
    db.execute('insert into test (t1, i1) values (?, ?)', ('two',2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('seven',7))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three',3))
    db.commit()  # commit changes

    '''/
    <sqlite3.Row object at 0x0000025E8C258B90>
    <sqlite3.Row object at 0x0000025E8C3B71B0>
    <sqlite3.Row object at 0x0000025E8C258B90>
    <sqlite3.Row object at 0x0000025E8C05A470>''' #address object location
    cursor = db.execute('select i1, t1 from test order by i1') 
    for row in cursor:
        print(row) #data comes in tuple form

    '''/
    {'i1': 1, 't1': 'one'}
    {'i1': 2, 't1': 'two'}
    {'i1': 3, 't1': 'three'}
    {'i1': 7, 't1': 'seven'}''' #dictionary VERY useful
    cursor = db.execute('select i1, t1 from test order by i1') 
    for row in cursor:
        print(dict(row)) #data comes in tuple form

    '''/
    one 1
    two 2
    three 3
    seven 7'''
    cursor = db.execute('select i1, t1 from test order by i1') 
    for row in cursor:
        print(row['t1'], row['i1']) #data comes in tuple form


if __name__ == "__main__": main()
