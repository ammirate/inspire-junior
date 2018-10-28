import os
import requests
from scraper.parser import ArticleParser
from backend.articles.api import smart_create_article


try:
    scraper_url = "http://{}:{}".format(
        os.environ['SCRAPER_SITE_1_PORT_5000_TCP_ADDR'],
        os.environ['SCRAPER_SITE_PORT_5000_TCP_PORT'],
    )
except KeyError:
    scraper_url = "http://0.0.0.0:8080"


class Scraper(object):

    def __init__(self, url=None):
        self.url = url or scraper_url
        self.parser = ArticleParser()

    def scrape(self):
        page = 0

        while True:
            scraped_content = self._run_scraper(page)
            articles_parsed = self.parser.parse_articles(scraped_content)

            if not articles_parsed:
                break

            self.store_articles(articles_parsed)
            page += 1

    def _run_scraper(self, page_number):
        url = self.url if page_number == 0 else self.url + '?page={}'.format(
            page_number)
        html = requests.get(url).text
        return html

    def store_articles(self, articles):
        for art in articles:
            print('creating article {}'.format(art['title']))
            smart_create_article(art)
