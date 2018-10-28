import requests
from scraper.parser import ArticleParser

URL = 'http://localhost:8080/'


class Scraper(object):

    def __init__(self, url):
        self.url = url
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
        url = URL if page_number == 0 else URL + '?page={}'.format(page_number)
        html = requests.get(url).text
        return html

    def store_articles(self, articles):
        print('STORING')
        print(articles)
