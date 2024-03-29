from Urlbuilder import Urlbuilder
from FlatPagePars import PageParser
from PageGetter import PageGetter
from constants import *
import csv
import bs4


class FlatParser:
    def __init__(self, interval = 100000, minPrice = 0, maxPrice = 100000000, filters = DEFAULT_FILTER, saveLinks = False, proxiesFile = None):
        self.maxPrice = maxPrice + 1
        self.minPrice = minPrice + 1
        self.soup = None
        self.page = None
        self.interval = interval
        self.builder = Urlbuilder()
        self.filters = filters
        self.saveLinks = saveLinks
        self.url = self.builder.get_url()
        self.links = []
        self.res = []
        self.nu = 0
        self.fieldnames = set()
        self.getter = PageGetter(proxiesFile=proxiesFile)
        self.pars = PageParser(proxiesFile=proxiesFile)
        self.builder.add_filters(self.filters)
        self.count = 0


    def getPage(self):
        self.page = self.getter.get_page(self.url)
        self.soup = bs4.BeautifulSoup(self.page.text, 'html.parser')


    def parsePriceInterval(self, minPrice, maxPrice):
        rooms = [1, 2, 3, 4, 5, 6, 9]

        self.links = []
        self.res = []

        for room in rooms:
            self.builder.clear()
            self.builder.add_price(minPrice, maxPrice)
            self.builder.add_room(room)
            self.url = self.builder.get_url()
            print(self.url)
            self.getPage()

            st = self.soup.find('h5', class_="_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_20px--fX7_V _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_14px--reQMB _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq")
            if st is None:
                continue

            s = st.text
            price = ""

            for i in s:
                if i.isdigit():
                    price += i

            flatCount = min(int(price), 28 * 54)
            self.count += flatCount

            for i in range(flatCount // 28):
                inf = self.soup.findAll('article', class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")
                for d in inf:
                    ninf = d.find('a', class_="_93444fe79c--link--eoxce")
                    href = ninf.get('href')
                    self.links.append(href)

                self.builder.next_page()
                self.url = self.builder.get_url()
                self.getPage()

            inf = self.soup.findAll('article', class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")

            for i in range(flatCount % 28):
                d = inf[i]
                ninf = d.find('a', class_="_93444fe79c--link--eoxce")
                href = ninf.get('href')
                self.links.append(href)

            self.parseFlats(room)


        if self.saveLinks:
            with open(f'links/links{self.nu}.txt', 'w') as f:
                for s in self.links:
                    f.write(s + "\n")
                f.close()


        with open(f'flats/flats{self.nu}.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()

            for i in self.res:
                writer.writerow(i)
            f.close()


        self.nu += 1


    def parseFlats(self, rooms):
        for i in self.links:
            res = self.pars.Parse(i)
            res['room'] = rooms
            self.res.append(res)

            for j in res.keys():
                self.fieldnames.add(j)

    def ParseAll(self):
        for i in range(self.minPrice, self.maxPrice, self.interval):
            print(self.count)
            self.parsePriceInterval(i, i + self.interval)
