"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    
    import argparse
    import collections
    import nltk
    from nltk.corpus import stopwords

    # read from file
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()
    print(f'\nТоп 100 слов из файла {arg.file}')
    try:
        with open(arg.file, encoding='UTF-8') as input_file:
            text_raw = input_file.read()
    except Exception:
        print('Ошибка чтения файла\n')
        exit()
    
    # preparation of lists
    stop_list = stopwords.words('english') + stopwords.words("russian")
    words_list = nltk.word_tokenize(text_raw.lower())

    words_list = [
        element_in_list for element_in_list in words_list 
        if element_in_list.isalpha()
        ]

    clean_words_list = [
        word for word in words_list 
        if word not in stop_list
        ]
    
    # counting results
    clean_words_list = collections.Counter( clean_words_list)
    
    for (count_line, word) in enumerate(clean_words_list.most_common(100)):
        print(f'{count_line + 1} {word[0]} ({word[1]} шт.)')