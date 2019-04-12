from bs4 import BeautifulSoup

import time
import requests
import urllib3
urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


class PChome:
    def __init__(self, query):
        self._url = 'https://www.pcstore.com.tw/adm/psearch.htm'
        self._url += '?store_k_word=JUU2JUIwJUEzJUU1JUJBJUE3&slt_k_option=1'
        self._data = {
            'ltg_p': ' ',
            'after_login': ' ',
            'slt_k_option': 1,
            'store_k_word': '%AE%F0%AEy'
        }

    def get_page(self):
        r = requests.post(self._url, data=self._data)
        r.encoding = 'big5'
        return BeautifulSoup(r.content, 'html.parser')
