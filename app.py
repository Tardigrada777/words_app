from csv import reader
from codecs import open
from random import randint
from numpy import unique
import eel

@eel.expose
def question():
     # Лист из всех определений слов 
    answers = []

    # Лист слов
    words = []

    with open('TOEFLWordBase.csv', 'r', encoding='utf-8', errors='ignore') as row_words:
        # Считываем содержимое файла в итерируемый объект
        reader_obj = reader(row_words)
        for row in reader_obj:
            answers.append(row[2])

            # Каждое слово - словарь со значениями
            # word              -> Само слово
            # translation       -> правильный перевод
            # part_of_speech    -> часть речи
            word = {
                'word': row[0],
                'translation': row[2],
                'part_of_speech': row[1]
            }
            words.append(word)

    # Случайное слово из общего списка
    index = randint(0, len(words)-1)
    word = words[index]

    # Создаем лист трех случайных чисел 
    # Проверяем, чтобы они все были разные
    a_indexes = []
    for i in range(0, 3):
            a_indexes.append(randint(0, len(answers) - 1))
    
    # Добавляем в список индексов ответов индекс текущего слова
    # Это нужно, чтобы другие варианты не повторяли правильный ответ
    a_indexes.append(index)

    # Проверяем на уникальность лист индексов
    # Все четыре индекса должны быть разные
    while len(unique(a_indexes)) != len(a_indexes):
        for i in range(0, 3):
            a_indexes.append(randint(0, len(answers) - 1))
    
    question = {
        'word': word['word'],
        'part_of_speech': word['part_of_speech'],
        'a': answers[a_indexes[0]],
        'b': answers[a_indexes[1]],
        'c': answers[a_indexes[2]],
        'd': answers[a_indexes[3]],
        'right_answ': word['translation']
    }

    return question

web_app_options = {
    'mode': "chrome-app", #or "chrome"
    'port': 8081,
}

eel.init('web')
eel.start('index.html', size=(900, 350), options=web_app_options)