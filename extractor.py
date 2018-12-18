import csv
import sqlite3


def extract_articles():
    with open("test%2Farticles.csv", "rt") as doc:
        dr = list(csv.reader(doc))
        for row in dr[1:]:
            print(row[0], row[1], row[2])
