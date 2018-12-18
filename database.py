import sqlite3


def generate_tables():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS project (projectid INTEGER PRIMARY KEY)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS articles ("+
        "token STRING PRIMARY KEY, project INTEGER, year INTEGER, country_name STRING," +
        "FOREIGN KEY (project) REFERENCES project(projectid))" )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits ("+
        "page_path STRING, query_string STRING, visit_country STRING)"
    )
    conn.commit()
    cur.close()
    conn.close()


def dummy_projects():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    for i in range(MAX_PROJECTS):
        cur.execute("insert into project (projectid) values({})".format(i))
    conn.commit()
    cur.close()
    conn.close()

def insert_articles(project, token, year, country_name):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    query = "insert into articles (project, token, year, country_name) values({},{},{},'{}')".format(project, token, year, country_name)
    cur.execute(query)
    cur.close()
    conn.close()
