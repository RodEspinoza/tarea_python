from database import generate_tables, dummy_projects
from extractor import extract_articles
def main():
    generate_tables()
    #dummy_projects()
    extract_articles()
    print("nani")
if __name__ == '__main__':
    main()
