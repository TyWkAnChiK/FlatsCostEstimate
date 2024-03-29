from constants import *

class Urlbuilder:
    def __init__(self, filters = None):
        if filters == None:
            self.filters = {'rooms' : set(), 'page' : 1}
        else:
            self.filters = filters

        if not 'page' in self.filters.keys():
            self.filters['page'] = 1

        self.url = BASE_URL + DEFAULT_PATH.format(self.filters['page'])
        self.other_filters = ""


    def add_room(self, rooms):
        self.filters['rooms'].add(rooms)

    def clear(self):
        self.filters = {'rooms': set(), 'minPrice': None, 'maxPrice': None, 'page' : 1}
        self.url = BASE_URL + DEFAULT_PATH.format(self.filters['page'])

    def add_price(self, mi, ma):
        self.filters['minPrice'] = mi
        self.filters['maxPrice'] = ma

    def add_page(self, page):
        self.filters['page'] = page

    def next_page(self):
        self.filters['page'] += 1

    def add_filters(self, filters):
        self.other_filters += filters

    def rebuild(self):
        self.url = BASE_URL + DEFAULT_PATH.format(self.filters['page'])

        if 'rooms' in self.filters.keys():
            for kol in self.filters['rooms']:
                kl = str(kol)
                if len(kl) == 1:
                    self.url += ROOM_PATH.format(kl)
                else:
                    self.url += STUDIO_PATH

        if 'minPrice' in self.filters.keys():
            self.url += MIN_PRICE_PATH.format(str(self.filters['minPrice']))

        if 'maxPrice' in self.filters.keys():
            self.url += MAX_PRICE_PATH.format(str(self.filters['maxPrice']))

        self.url += self.other_filters


    def get_url(self):
        self.rebuild()
        return self.url

