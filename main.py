import json
from scraper.scraper import scrape, result
from summary.summarize import summarize

def append_summarized_articles():
    data = scrape(["trp", "scam", "english"])
    master_article = ""
    for key in data:
        master_article += summarize(data[key])
    
    with open("master_article.txt", "w") as f:
        f.write(master_article)
        f.close()

def main():    
    append_summarized_articles()

if __name__ == "__main__":
    main()