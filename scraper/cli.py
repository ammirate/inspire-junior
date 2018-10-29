from __future__ import absolute_import, division, print_function

import click
import os
import requests

from api import Scraper


@click.group()
def scraper():
    pass


def _get_scraping_url():
    try:
        scraper_url = "http://{}:{}".format(
            os.environ['SCRAPER_SITE_1_PORT_5000_TCP_ADDR'],
            os.environ['SCRAPER_SITE_PORT_5000_TCP_PORT'],
        )
    except KeyError:
        scraper_url = "http://0.0.0.0:8080"

    return scraper_url


@scraper.command()
def ping():
    scraping_url = _get_scraping_url()
    click.echo('Pinning Inspire on %s' % scraping_url)
    resp = requests.get(scraping_url)
    click.echo('Got response %d' % resp.status_code)


@scraper.command()
def env():
    env = {k: v for (k, v) in os.environ.items()}
    click.echo(env)


@scraper.command()
def run():
    scraping_url = _get_scraping_url()
    click.echo('Scraping %s...' % scraping_url)

    s = Scraper(scraping_url)
    total = s.run()

    click.echo('Scraped %d articles' % total)


if __name__ == '__main__':
    scraper()
