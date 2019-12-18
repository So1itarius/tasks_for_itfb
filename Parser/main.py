from Parser.csv_parser import csv_creater, csv_reader
from Parser.p_utils import get_html, speed_searcher, probability_searcher, save_line, info_arr

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
    get_weather_info()
    csv_creater(info_arr)
    csv_reader()
