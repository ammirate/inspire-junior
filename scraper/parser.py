from __future__ import absolute_import, division, print_function

from bs4 import BeautifulSoup

ARTICLE_TAG = 'div'
ARTICLE_CLASS = 'post'

TITLE_TAG = 'h2'
TITLE_CLASS = 'post-title'

ABSTRACT_TAG = 'p'
ABSTRACT_CLASS = 'post-description'

CATEGORY_TAG = 'div'
CATEGORY_INNER_TAG = 'span'
CATEGORY_CLASS = 'post-categories'


class ArticleParser(object):

    def __init__(self):
        self.soup = None

    def _first(self, nodes):
        try:
            return nodes[0].text
        except KeyError:
            return ''

    def _parse_category(self, article_soup):
        category_node = article_soup.findAll(CATEGORY_TAG, {'class': CATEGORY_CLASS})
        categs = self._first(category_node)
        return ''.join((categs).split())  # removes \n \r

    def _parse_article(self, article_soup):
        title = self._first(article_soup.findAll(TITLE_TAG, {'class': TITLE_CLASS}))
        abstract = self._first(
            article_soup.findAll(ABSTRACT_TAG, {'class': ABSTRACT_CLASS})
        )
        category = self._parse_category(article_soup)
        return {
            "title": title,
            "abstract": abstract,
            "category": category
        }

    def parse_articles(self, html):
        self.soup = BeautifulSoup(html)

        articles = []
        article_divs = self.soup.findAll(ARTICLE_TAG, {'class': ARTICLE_CLASS})

        for div in article_divs:
            article = self._parse_article(div)
            articles.append(article)

        return articles
