import bs4
from PageGetter import PageGetter

class PageParser:
    def __init__(self, url = None, proxiesFile = None):
        self.url = url
        self.getter = PageGetter(proxiesFile=proxiesFile)
        self.page = None
        self.soup = None

    def getPage(self):
        self.page = self.getter.get_page(self.url)
        self.soup = bs4.BeautifulSoup(self.page.text, 'html.parser')


    def parseData(self):
        inf = self.soup.findAll('div', class_="a10a3f92e9--item--qJhdR")

        data = {}

        for d in inf:
            spans = d.findAll('span')
            if len(spans) == 2:
                name = d.find('span')
                val = name.findNext()
                txt = ""

                for i in str(val.text):
                    if i == '\xa0':
                        break
                    else:
                        txt += i

                data[name.text] = txt
            else:
                name = d.find('p')
                val = name.findNext()
                txt = ""

                for i in str(val.text):
                    if i == '\xa0':
                        break
                    else:
                        txt += i

                data[name.text] = txt

        inf = self.soup.findAll('div', class_="a10a3f92e9--item--Jp5Qv")

        for d in inf:
            ninf = d.find('div', class_="a10a3f92e9--text--eplgM")
            spans = ninf.findAll('span')

            if len(spans) == 2:
                name = ninf.find('span')
                val = name.findNext()
                txt = ""

                for i in str(val.text):
                    if i == '\xa0':
                        break
                    else:
                        txt += i

                data[name.text] = txt
            else:
                name = ninf.find('p')
                val = name.findNext()
                txt = ""

                for i in str(val.text):
                    if i == '\xa0':
                        break
                    else:
                        txt += i

                data[name.text] = txt

        pr = self.soup.find('div', class_="a10a3f92e9--price--Pg6fn")
        price_ht = pr.find('span')
        price = ""

        for i in str(price_ht.text):
            if i.isdigit():
                price += i

        price = int(price)
        data['Цена'] = price

        inf = self.soup.findAll('li', class_="a10a3f92e9--underground--pjGNr")

        data['Метро'] = {}

        for d in inf:
            name = d.find('a', class_="a10a3f92e9--underground_link--VnUVj")
            tim = d.find('span', class_="a10a3f92e9--underground_time--YvrcI")

            rt = ""

            for c in str(tim.text):
                if c.isdigit():
                    rt += c

            pat = tim.find('path')
            st = str(pat)

            if st.count('4.427c.127.03.26.044.395.044Z') > 0:
                data['Метро'][name.text] = (rt, 'leg')
            else:
                data['Метро'][name.text] = (rt, 'car')

        data['link'] = self.url

        return data


    def Parse(self, url = None):
        if url != None:
            self.url = url
        self.getPage()
        return self.parseData()
