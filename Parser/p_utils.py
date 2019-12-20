import requests
import re

info_arr = []


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.103 Safari/537.36'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def speed_searcher(text):
    # Ищем информацию о скорости ветра, начиная со слов "ветер" и до м/с.
    result = re.search(r'[Вв]етер.+м/с\.', text)
    return result.group(0)


def probability_searcher(text):
    # Ищем информацию о вероятности осадков, начиная со слов "вероятность" и до %.
    result = re.search(r'[Вв]ероятность.+%\.', text)
    return result.group(0)


def save_line(a, b, c, d):
    # Форма для заполнения массива информации
    dict = {"weekday": a,
            "temperature": b,
            "speed": c,
            "probability": d}
    info_arr.append(dict)
