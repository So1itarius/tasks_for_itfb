import matplotlib.pyplot as plt
import numpy as np

import requests


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


def diagram(d):
    jet = plt.cm.jet
    colors = jet(np.linspace(0, 1, len(d)))

    fig, ax = plt.subplots()

    for i, color in zip(d, colors):
        x = i
        y = d[i]
        ax.scatter(x, y, color=color, s=90, marker='*')
        ax.get_xaxis().get_major_formatter()
        fig.autofmt_xdate()
        plt.xticks(x, "")
        plt.legend(d.keys())

    plt.subplots_adjust(bottom=.24, right=.98, left=0.03, top=.89)
    plt.grid()
    plt.show()
