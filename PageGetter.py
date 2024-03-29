import requests
import time
import random
from cfscrape import create_scraper

class PageGetter:
    def __init__(self, proxiesFile = None):
        self.proxies = []
        session = requests.Session()
        session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru,en-US;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}

        self.session = create_scraper(session)


        if proxiesFile is not None:
            with open(proxiesFile, 'r') as f:
                s = f.readline()
                while s != "":
                    self.proxies.append({'http' : "socks5://" + s[:-1], 'https' : "socks5://" + s[:-1]})
                    s = f.readline()

                f.close()


    def get_page(self, url):
        if not self.proxies:
            while True:
                try:
                    page = self.session.get(url)
                    page.raise_for_status()
                    return page
                except:
                    time.sleep(5)
                    print('default')
        else:
            while True:
                proxy = random.choice(self.proxies)
                try:
                    page = requests.get(url, proxies=proxy)
                    print(page.status_code)
                    page.raise_for_status()
                    return page
                except:
                    time.sleep(1)
                    print(proxy)
