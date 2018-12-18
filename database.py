import sqlite3

def generate_tables():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE project (projectid INTEGER PRIMARY KEY)")
    cur.execute(
        "CREATE TABLE articles ("+
        "token STRING PRIMARY KEY, project INTEGER, year INTEGER, country_name STRING)" +
        "FOREING KEY (project) REFERENCES project(projectid)" )
    conn.commit()
    cur.close()
