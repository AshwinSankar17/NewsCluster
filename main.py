from csv_df import create_csv
from cluster import cluster
from to_db import to_database

# LINKS = ['http://cnn.com', 'https://www.hindustantimes.com/', 'https://timesofindia.indiatimes.com/']

if __name__ == "__main__":
    '''
        Run this file and you run every other file
        The driver code for the whole project
    '''
    create_csv()
    cluster()
    to_database()