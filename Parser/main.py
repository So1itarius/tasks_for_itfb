from csv_utils import csv_creater, csv_reader
from p_utils import get_html, speed_searcher, probability_searcher, save_line, info_arr
"""
PyCharm предлагает импортировать, указывая полный путь через точку, например Parser.csv_utils и если имя изменить,
то он будет подчеркивать "красным", но все равно запускать. Если оставить полное имя, то он не сможет запускатся
через консоль, указывая на то, что модуля Parser не существует...При запуске через консоль файл .csv появляется в
общем дереве проекта

"""


from bs4 import BeautifulSoup


def get_weather_info():
    html = get_html("https://dfedorov.spb.ru/python3/ya_forecast.html")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_info = soup.find('body').findAll('div', class_='row row-forecast')
        for info in all_info:
            weekday = info.find('div', class_='forecast-label').text
            temperature = info.find('em').text + " градусов"
            speed = speed_searcher(info.find('div', class_='forecast-text').text)
            probability = probability_searcher(info.find('div', class_='forecast-text').text)
            save_line(weekday, temperature, speed, probability)


if __name__ == "__main__":
    # Парсим погоду и заполняем массив с информацией
    get_weather_info()
    # Создаем .csv файл и заполняем его массивом с информацией
    csv_creater(info_arr)
    # Выводим информацию в консоль для проверки
    csv_reader()
