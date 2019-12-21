import collections

from bs4 import BeautifulSoup
from natasha import NamesExtractor

from utils import diagram
from Parser.p_utils import get_html
"""
Такая же проблема с импортом, что и в задаче 1.
"""

# full_text = ""

result = []


def n_searcher(text):
    # Ищет имена и заполняет результирующий список прямо объектами целиком, сконвертироваными в строку
    # т.к. не ясно как лучше вынимать и сравнивать (first,middle,last,nick) элементы имени.
    global result
    extractor = NamesExtractor()
    matches = extractor(text)
    for match in matches:
        result.append(str(match.fact))
        # print(match.fact)


def draw_graph(dict):
    res = collections.Counter(dict)
    for key, value in res.items():
        print(key, value)
    diagram(res)


def get_yandex_href():
    html = get_html("https://yandex.ru/news/export")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_info = soup.find('div', class_='tabs-panes export__select-panes i-bem').findAll('div',
                                                                                            class_='export__letter')
        for info in all_info:
            allhref = info.findAll('a', class_='link link_theme_normal i-bem')
            for href in allhref:
                n_searcher(get_html(href["href"]))


if __name__ == "__main__":
    # Парсим яндекс и собираем все новости, во всех категориях.Заполняем масссив всеми найдеными именами
    get_yandex_href()
    # Подсчитываем слова и рисуем график, для удобства выводим имена в консоль
    draw_graph(result)
