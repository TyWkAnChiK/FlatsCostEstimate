import bs4
import urllib.request


class Proxy:
    def __init__(self, proxies):
        self.proxies = []
        if proxies is not None:
            self.proxies = proxies

    def check_captcha(self, url):
        page = bs4.BeautifulSoup(url, 'html.parser')
        return page.text.find('Captcha') == 0

    def check(self, proxy, url):
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({'https': proxy}))
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)

        try:
            html = urllib.request.urlopen(urllib.request.Request(url))
        except:
            return False

        return True

    def get_proxy(self, url):
        uk = 0
        while len(self.proxies) > uk:
            proxy = self.proxies[uk]
            if self.check(proxy, url) and self.check_captcha(url):
                return proxy
