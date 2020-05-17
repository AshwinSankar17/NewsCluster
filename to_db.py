import sqlite3
from sqlite3 import IntegrityError
import csv

def insert_to_db(tup):
    with sqlite3.connect('./data/NEWS.DB') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO content (headlines, news) VALUES(?, ?);", tup)
        con.commit()

def to_database():
    '''
        converts csv to db
    '''
    with sqlite3.connect('./data/NEWS.DB') as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS content(headlines TEXT, news TEXT);')
        with open('./data/NewsCluster.csv', encoding='utf-8') as fin:
            dr = csv.DictReader(fin)
            for i in dr:
                try:
                    tup = (i['Title'], i['News'])
                    insert_to_db(tup)
                except IntegrityError as ie:
                    if 'unique constraint' in ie:
                        continue

            # to_db = [(i['Title'], i['News']) for i in dr]
        
        # cur.executemany("INSERT INTO content (headlines, news) VALUES(?, ?);", to_db)
        con.commit()
    con.close()

def print_db():
    '''
        prints database
        used for reference and verification
    '''
    with sqlite3.connect("./data/NEWS.DB") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM content')
        return cur.fetchall()

# if __name__ == "__main__":
    '''
    execute either of the functions to update database or displahy the content
    '''
    # to_database()
    # print(print_db()[0])