#!/usr/bin/python3
# sqlite3-crud.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

# Insert is same as create
def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

# Retrieve used in dictionary
def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()

# Update values
def update(self, row): #self and db are interchangeable values, its just first arg = object passed
    self.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1'])) # must pass in list or tuple
    self.commit()

# deletes
def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()

# Outputs current data
def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test3.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')

    '''/Create rows
    four: 4
    one: 1
    three: 3
    two: 2'''
    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1))
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db)

    '''/Retrieve rows
    {'t1': 'one', 'i1': 1} {'t1': 'two', 'i1': 2}'''
    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    '''/Update rows
    four: 4
    one: 101
    three: 103
    two: 2'''
    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)

    '''/Delete rows
    four: 4
    two: 2'''
    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()
