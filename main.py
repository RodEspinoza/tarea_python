from database import generate_tables, dummy_projects, clean_tables, get_top_ten_proyects, get_top_by_visit_country
from extractor import extract_articles, extract_visits

MAX_PROJECTS = 20


def main():
    #generate_tables()
    #clean_tables()
    #dummy_projects(MAX_PROJECTS)
    #extract_articles(MAX_PROJECTS)
    #extract_visits()
    get_top_ten_proyects()
    get_top_by_visit_country("RU")

if __name__ == '__main__':
    main()
