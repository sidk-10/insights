import requests
from bs4 import BeautifulSoup
import json
import os

DIR = os.path.dirname(__file__)

def fetch_search_results(keywords):
    article_links = []
    url = "https://www.google.com/search?q={}&tbm=nws".format("+".join(keywords))
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    index = 0
    for link in page.find_all("a"):
        if index % 2 == 0:
            try:
                article_url = link.get("href").split("/url?q=")[1].split("&")[0] 
                # print(article_url)
                # if article_url[-1] == "/": article_url = article_url[:-1]
                article_links.append(article_url)
                # article = BeautifulSoup(article_page, 'html.parser')
            except Exception as error:
                error = error
        else: pass
        index += 1
    # print(article_links)
    for link in article_links:
        print(link)
    return article_links

def fetch_articles(article_links):
    # print(article_links)
    # return
    articles = {}
    for index, link in enumerate(article_links):
        if index > 4: break
        agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        response = requests.get(link, headers=agent)
        page = BeautifulSoup(response.text, 'html.parser')
        page = clean_article(page, link.split("://")[1].split("/")[0].split(".")[0])
        article = ""
        for line in page.get_text():
            article += line.rstrip("\n")
        articles[link] = article
        with open(os.path.join(DIR, "data/article{}.html".format(index + 1)), "w") as f:
            f.write(page.prettify())
            f.close()
    print(articles)
    return articles

def clean_article(page, publisher):
    with open(os.path.join(DIR, "rules.json"), "r") as f:
        rules = json.load(f)
        f.close()
    rules = rules
    try:
        for x in page.find_all(rules[publisher]["elements"]):
            x.extract()
        for clas in rules[publisher]["classes"]:
            for x in page.find_all(class_=clas):
                x.extract()
    except: pass
    for x in page.find_all(rules["common"]["elements"]):
        x.extract()
    for x in page.find_all():
        if len(x.get_text(strip=True)) == 0:
            x.extract()
    return page

def result():
    with open(os.path.join(DIR, "data/articles.json"), "r") as f:
        data = json.load(f)
    return data

def scrape(keywords=["the", "central", "vista", "project"]):
    article_links = fetch_search_results(keywords)
    articles = fetch_articles(article_links)
    with open(os.path.join(DIR, "data/articles.json"), "w+") as f:
        json.dump(articles, f, indent=4)
        f.close()
    return result()

if __name__ == "__main__":
    article_links = fetch_search_results(["the", "central", "vista", "project"])
    articles = fetch_articles(article_links)
    with open(os.path.join(DIR, "data/articles.json"), "w+") as f:
        json.dump(articles, f, indent=4)
        f.close()
    # print(articles)
