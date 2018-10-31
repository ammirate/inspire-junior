Inspire-Junior
=================

[![Build Status](https://travis-ci.com/ammirate/inspire-junior.svg?branch=master)](https://travis-ci.com/ammirate/inspire-junior)
[![Coverage Status](https://coveralls.io/repos/github/ammirate/inspire-junior/badge.svg)](https://coveralls.io/github/ammirate/inspire-junior)
[![LICENSE](https://img.shields.io/github/license/inspirehep/inspirehep-search-js.svg)](https://github.com/inspirehep/inspirehep-search-js/blob/master/LICENSE)

Inspire-Junior is a basic application, based on Docker containers, that scrapes a fake HEP repository, and displays the scraped articles in a React application. The communication between the apps is based on REST Apis.
There are 4 main actors:
1) The fake HEP repo, which is an instance of the *docker* image `drjova/article-data-codereview`
2) The `backend` that provides REST Apis to store and retrieve articles
3) The `frontend`, a *React* app to display and filter articles by categories
4) The `scraper` CLI

Installation
------------
First, you need to install the packages to build the *frontend* app:
    
    $ cd react_app
    $ npm install
    
Now, assuming you are using *docker-compose*:
    
    $ cd ..
    $ docker-compose up

Demo
----
After spinning up the *docker* containers you can navigate to the exposed URLs to ciew the applications running.
Navigate to `http://localhost:8080` to see the `fake HEP repo`.
Navigate to `http://localhost:5555` to see the `REST Api`.
Navigate to `http://localhost:3000` to see the `React App`.

Tests
-----
Inside a virtualenvironment, run:

    $ ./run-test.sh

How to use?
-----------
The goal of the project is to demonstrate how the scraper CLI fetches articles from the fake HEP repo, sends them via to the *backend* so they can be displayed by the *frontend*.

All you need to do is connect into the *scraper* container and run the CLI command to start the scraping. After it finishes, you will see in the *frontend* app the same articles provided by the fake HEP repo.

    $ docker-compose exec scraper sh
    $ python scraper/cli.py run
