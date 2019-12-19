from nltk.stem import SnowballStemmer

snowball_stemmer = SnowballStemmer("russian")
i = 0
with open('texts_opinions.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(' ')
        print(line)
        for word in line:
            #word = line[0]
            #wordCount = line[1]
            stem = snowball_stemmer.stem(word)
            print(word, ''.join(stem))


