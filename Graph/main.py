import collections

from bs4 import BeautifulSoup
from natasha import NamesExtractor

from Graph.utils import diagram
from Parser.p_utils import get_html

# full_text = ""

result = []


def n_searcher(text):
    global result
    extractor = NamesExtractor()
    matches = extractor(text)
    for match in matches:
        result.append(str(match.fact))
        # print(match.fact)


def count_name(dict):
    res = collections.Counter(dict)
    for key, value in res.items():
        print(key, value)
    diagram(res)


def get_yandex_href():
    global full_text
    html = get_html("https://yandex.ru/news/export")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_info = soup.find('div', class_='tabs-panes export__select-panes i-bem').findAll('div',
                                                                                            class_='export__letter')
        # print(all_info)
        for info in all_info:
            allhref = info.findAll('a', class_='link link_theme_normal i-bem')
            for href in allhref:
                n_searcher(get_html(href["href"]))


if __name__ == "__main__":
    get_yandex_href()
    count_name(result)
