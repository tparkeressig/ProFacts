import sqlite3
from random import random, randint, choice
from json import dump

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def random_name(length):
    return ''.join([choice(alphabet) for i in range(length)])

def random_float(lower, upper):
    return (upper - lower) * random() + lower

def sql_to_json(cursor, file, keys, table):
    cursor.execute('select ' + ','.join(keys) + ' from ' + table)
    l = []
    for row in cursor.fetchall():
        l.append({key: entry for (key, entry) in zip(keys, row)})
    dump(l, file, indent=4)

def generate_random_data(cursor):
    for i in range(100):
        cursor.execute('insert into restaurants values (?, ?, ?, ?)', [random_name(randint(10, 30)),
                                                                      random_float(-180, 180),
                                                                      random_float(-180, 180),
                                                                      random_float(0, 10)])

if __name__ == '__main__':

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    #generate_random_data(cursor)
    #conn.commit()
    
    sql_to_json(cursor, open('example.json', 'w'), ['name', 'lat', 'lon', 'danger_rating'], 'restaurants')