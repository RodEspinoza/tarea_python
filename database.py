import sqlite3

database_name = "test.db"


def generate_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS project (projectid INTEGER PRIMARY KEY)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS articles ("+
        "token STRING PRIMARY KEY, project INTEGER, year INTEGER, country_name STRING," +
        "FOREIGN KEY (project) REFERENCES project(projectid))" )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits ("+
        "page_path STRING, query_string STRING, visit_country STRING)")
    conn.commit()
    cur.close()
    conn.close()


def clean_tables():
    tables = ['visits', 'articles', 'project']
    conn = get_connection()
    cur = conn.cursor()
    for table in tables:
        cur.execute("delete from {}".format(table))
    conn.commit()
    cur.close()
    conn.close()


def dummy_projects(MAX_PROJECTS):
    conn = get_connection()
    cur = conn.cursor()
    for i in range(MAX_PROJECTS):
        cur.execute("insert into PROJECT (projectid) values({})".format(i))
    conn.commit()
    cur.close()
    conn.close()


def insert_articles(project, token, year, country_name):
    conn = get_connection()
    cur = conn.cursor()
    query = "insert into ARTICLES (project, token, year, country_name) values({},{},{},'{}')".format(
        project, token, year, country_name)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def insert_visit(page_path, query_string, visit_country):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    query = "insert into VISITS (page_path, query_string, visit_country) values('{}', '{}', '{}')".format(page_path, query_string, visit_country)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def get_top_ten_proyects():
     #"select ar.token, ar.project , count(v.rowid) as row_count from articles as ar join  visits as v  on v.page_path  LIKE '%' || ar.token || '%' group by ar.token, ar.project;"
    conn = get_connection()
    cur = conn.cursor()
    query = "select pj.projectid, (select count(v.rowid) as row_count from articles as ar join visits as v on v.page_path LIKE '%' || ar.token || '%'  where ar.project = pj.projectid ) as total_visits  from project as pj order by total_visits desc limit 10"
    cur.execute(query)
    rows = cur.fetchall()
    print("Top ten projects ")
    for row in rows:
        print("Project_id :  {}, Total_visits : {}".format(row[0], row[1]))
    cur.close()
    conn.close()



def get_top_by_visit_country(visit_country):
        conn = get_connection()
        cur = conn.cursor()
        query = "select pj.projectid, (select count(v.rowid) as row_count from articles as ar join visits as v on v.page_path LIKE '%' || ar.token || '%'  where ar.project = pj.projectid and v.visit_country = '{}') as total_visits  from project as pj order by total_visits desc limit 10".format(visit_country)
        cur.execute(query)
        rows = cur.fetchall()
        print("Top ten projects by country: {}".format(visit_country))
        for row in rows:
            print("Project_id :  {}, Total_visits : {}".format(row[0], row[1]))
        cur.close()
        conn.close()



def custom_query():
    #work withs utm codes
    return ""

def get_connection():
    return sqlite3.connect(database_name)
