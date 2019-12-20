import re

from nltk.stem import SnowballStemmer

from reviews_classification.patterns import POSITIVE, NEGATIVE

snowball_stemmer = SnowballStemmer("russian")


def converter(arr):
    i = 0
    for word in arr:
        stem = snowball_stemmer.stem(word)
        arr[i] = stem
        i += 1
    return arr


with open('texts_opinions.txt', 'r', encoding='utf-8') as f:
    with open('texts_ratings.txt', 'r', encoding='utf-8') as f1:
        con_pos = converter(POSITIVE)
        con_neg = converter(NEGATIVE)
        for line, line1 in zip(f, f1):
            rep = re.sub(r'[!\"#$%&\'(\-)*+,›./:;<=>?@[\]^_\\`{|}~]', '', line)
            line = rep.strip().lower().split(' ')
            p = 0
            n = 0
            for word in converter(line):
                if word in con_pos:
                    p += 1
                elif word in con_neg:
                    n += 1
            if p > n:
                print(f"Результат обработки: positive, «правильная» классификаци: {line1}")
            elif p < n:
                print(f"Результат обработки: negative, «правильная» классификаци: {line1}")
            else:
                print(f"Результат обработки: undef, «правильная» классификаци: {line1}")
