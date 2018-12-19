from database import *
from extractor import extract_articles, extract_visits

MAX_PROJECTS = 20


def main():
    generate_tables()
    clean_tables()
    dummy_projects(MAX_PROJECTS)
    extract_articles(MAX_PROJECTS)
    extract_visits()
    get_top_ten_proyects()
    get_top_by_visit_country("RU")
    get_top_ten_proyects_and_source("Whatsapp")
if __name__ == '__main__':
    main()
