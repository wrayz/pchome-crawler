from bs4 import BeautifulSoup

import requests
import urllib3
urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


class PChome:
    def __init__(self, query):
        self._url = 'https://www.pcstore.com.tw/'
        self._query = query

    def get_page(self):
        r = requests.get(self._url)
        r.encoding = 'big5'
        return BeautifulSoup(r.text, 'html.parser')
