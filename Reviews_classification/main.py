import re

from nltk.stem import SnowballStemmer

from config import POSITIVE, NEGATIVE, texts_opinions, texts_ratings

# Такая же ошибка с импортом, как и в предидущих файлах


snowball_stemmer = SnowballStemmer("russian")


def converter(arr):
    # Приводим слова в массиве к "начальной форме"
    i = 0
    for word in arr:
        stem = snowball_stemmer.stem(word)
        arr[i] = stem
        i += 1
    return arr


with open(texts_opinions, 'r', encoding='utf-8') as f1:
    with open(texts_ratings, 'r', encoding='utf-8') as f2:
        con_pos = converter(POSITIVE)
        con_neg = converter(NEGATIVE)
        for line1, line2 in zip(f1, f2):
            # убираем все символы
            rep = re.sub(r'[!\"#$%&\'(\-)*+,›./:;<=>?@[\]^_\\`{|}~]', '', line1)
            line = rep.strip().lower().split(' ')
            # Создаем счетчики положительных и отрицательных слов
            p = 0
            n = 0
            for word in converter(line):
                if word in con_pos:
                    p += 1
                elif word in con_neg:
                    n += 1
            if p > n:
                print(f"Результат обработки: positive, «правильная» классификаци: {line2}")
            elif p < n:
                print(f"Результат обработки: negative, «правильная» классификаци: {line2}")
            else:
                print(f"Результат обработки: undef, «правильная» классификаци: {line2}")
