import pip._vendor.requests as requests
from bs4 import BeautifulSoup
import random


def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    # id here refers to the HTML id tag
    title = soup.find(id="firstHeading")
    print(title.text)

    # Get all the links
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wikipedia articles
        if link['href'].find("/wiki/") == -1:
            continue

        linkToScrape = link
        break
    # print(linkToScrape)

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])


scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
