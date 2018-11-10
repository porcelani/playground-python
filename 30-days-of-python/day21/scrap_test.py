# coding: utf-8
import requests
from bs4 import BeautifulSoup

# virtualenv -p python3 scrape && scrape

# http://docs.python-requests.org/en/master/

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = "https://google.com.br"


def test_scrap_request():
    response = requests.get(url)

    assert response.status_code is 200

    soup = BeautifulSoup(response.text)
    print soup

    find_all = soup.findAll("a")
    assert len(find_all) > 10


def test_beautiful_soup():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print soup.prettify()
