import os
import requests
from __future__ import absolute_import, division, print_function

from parser import ArticleParser


def _get_api_post_url():
    try:
        api_url = "http://{}:{}".format(
            os.environ['BACKEND_1_PORT_5555_TCP_ADDR'],
            os.environ['BACKEND_1_PORT_5555_TCP_PORT'],
        )
    except KeyError:
        api_url = "http://0.0.0.0:5555"

    return api_url + "/api/articles?smart=true"


class Scraper(object):

    def __init__(self, target_site_url):
        self.url = target_site_url
        self.api_url = _get_api_post_url()
        self.parser = ArticleParser()

    def run(self):
        page = 0
        total = 0

        while True:
            scraped_content = self._run_scraper(page)
            articles_parsed = self.parser.parse_articles(scraped_content)

            if not articles_parsed:
                break

            total += len(articles_parsed)
            self.store_articles(articles_parsed)
            page += 1

        return total

    def _run_scraper(self, page_number):
        url = self.url if page_number == 0 else self.url + '?page={}'.format(page_number)
        html = requests.get(url).text
        return html

    def store_articles(self, articles):
        for art in articles:
            requests.post(self.api_url, json=art)
