import csv
import sqlite3
import random
import re

def extract_articles(MAX_PROJECTS):
    from database import insert_articles
    with open("test%2Farticles.csv", "rt") as doc:
        dr = list(csv.reader(doc))
        for row in dr[1:]:
            possible_project = random.randint(1, MAX_PROJECTS)
            insert_articles(possible_project, row[0], row[1], row[2])

def extract_visits():
    from database import insert_visit
    with open("test%2Fvisits.csv", "rt") as doc:
        dr = list(csv.reader(doc))
        for row in dr[1:]:
            #article_id = re.search('/(.*)/', row[0]).group(1)
            insert_visit(row[0], row[1], row[2])
