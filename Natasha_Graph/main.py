import collections
import re

from bs4 import BeautifulSoup
from natasha import NamesExtractor

from utils import diagram, get_html

"""
Такая же проблема с импортом, что и в задаче 1.
Из за этого приходится дублировать функции
"""


result = []


def pattern(str):
    res = re.findall(r'first=[\'\w]+,|last=[\'\w]+,', str)
    f = "" if res[0].replace("'", "").replace(",", "").split("=")[1] == "None" else \
        res[0].replace("'", "").replace(",", "").split("=")[1]
    l = "" if res[1].replace("'", "").replace(",", "").split("=")[1] == "None" else \
        res[1].replace("'", "").replace(",", "").split("=")[1]
    return (f + " " + l).strip()


def n_searcher(text):
    # Ищет имена и заполняет результирующий список прямо объектами целиком, сконвертироваными в строку
    # т.к. не ясно как лучше вынимать и сравнивать (first,middle,last,nick) элементы имени.
    global result
    extractor = NamesExtractor()
    matches = extractor(text)
    app = result.append
    for match in matches:
        app(pattern(str(match.fact)))


def draw_graph(lst):
    res = collections.Counter(lst).most_common(20)
    dict = {}
    for item in res:
        dict[item[0]] = item[1]
        print(item[0], item[1])
    diagram(dict)


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
    # Медленно работает из за объема данных или алгоритма
    get_yandex_href()
    # Подсчитываем слова (топ 20) и рисуем график, для удобства выводим имена в консоль
    draw_graph(result)
