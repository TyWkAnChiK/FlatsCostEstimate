# FlatsCostEstimate
# CianParser
Парсер данных с cian.ru

# Файлы и их содержание
* constants.py
Константные куски url, используемые для его сборки
* Urlbuilder
Класс для создания url с фильтрами, ценовым диапазоном и т.д.
* PageGetter
Класс для запроса страницы, использует прокси и clouflare для обхода блокировок
* FlatPagePars
Класс для сбора всей информации со страницы квартиры
* FlatParser
Класс, используемый для парсинга

### Установка библиотек
```bash
pip install beautifulsoup4
pip install requests
pip install cfscrape
```

### Использование
```python
from FlatParser import FlatParser

parser = FlatParser(saveLinks = True, proxiesFile = 'proxies.txt')
parser.ParseAll()

```

### Инициализация
Параметры, используемые при инициализации парсера:
* minPrice  maxPrice, interval - Диапазон цен и интервал для перебора по ценам(используется для обхода ограничения в 54 страницы)_
* filters - строка фильтров(собирается из файла constants)
* saveLinks - если True, то сохраняет ссылки на квартиры для каждого интервала в links
* proxiesFile - путь до txt файла с прокси в формате {login}:{password}@{ip}:{port}. Если None, то запросы делаются со своего ip

### Результат
Для каждого интервала сохраняется в отдельном csv в flats
