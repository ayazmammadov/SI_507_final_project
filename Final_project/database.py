import sqlite3
import csv
import json
import sys


DATABASE_NAME = 'imbd_movie.db'
DATA_CSV = 'movie_data.csv'


conn = sqlite3.connect(DATABASE_NAME)
cur = conn.cursor()


statement = "DROP TABLE IF EXISTS 'Genre';"
cur.execute(statement)
statement = "DROP TABLE IF EXISTS 'Movie';"
cur.execute(statement)
conn.commit()


# Create tables from JSON

statement = """
    CREATE TABLE 'Genre' (
        'Id' INTEGER PRIMARY KEY,
        'Genre' TEXT
    );
"""
cur.execute(statement)
conn.commit()




statement = """
    CREATE TABLE 'Movie' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'MovieName' TEXT,
        'Director' TEXT,
        'Actor' TEXT,
        'ReleaseDate' INTEGER,
        'MovieRef' TEXT,
        'MovieLinkGenre' INTEGER,
        FOREIGN KEY(MovieLinkGenre) REFERENCES Genre(Id)
    );"""

cur.execute(statement)
conn.commit()

#  Populating CSV file

csv_file = open(DATA_CSV,encoding='utf8')
csv_data = csv.reader(csv_file)


for line in csv_data:
    if line[0] != "movieName":
        insertion = (None, line[3])
        statement = 'INSERT INTO "Genre" '
        statement += 'VALUES (?, ?)'

        cur.execute(statement, insertion)
conn.commit()

csv_file = open(DATA_CSV,encoding='utf8')
csv_data = csv.reader(csv_file)

for line in csv_data:
    if line[0] != "movieName":
        insertion = (None, line[0], line[1],line[2],line[-1],line[-2],line[3])
        statement = 'INSERT INTO "Movie" '
        statement += 'VALUES (?, ?, ? , ? , ? ,?, ? )'
        cur.execute(statement, insertion)
conn.commit()



state_MovieLinkGenre = '''
        UPDATE Movie
        SET (MovieLinkGenre) = (SELECT c.ID FROM Genre c WHERE Movie.MovieLinkGenre = c.Genre)
    '''

cur.execute(state_MovieLinkGenre)
conn.commit()
def question():
    lines = cur.execute('SELECT movieName FROM "Movie" WHERE director= "Steven Spielberg (dir.)"')
    for line in lines:
        print(line[0])
    pass
question()
conn.close()

