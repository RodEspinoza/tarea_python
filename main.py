from database import generate_tables, dummy_projects
from extractor import extract_articles

MAX_PROJECTS = 20

def main():
    generate_tables()
    dummy_projects(MAX_PROJECTS1)
    extract_articles(MAX_PROJECTS)
    print("nani")
if __name__ == '__main__':
    main()
