import csv
import codecs
import os
import random
import numpy

def main():
    data = read_from_file()
    words_list = data['words']
    answers = data['answers']
    answer = 'yes'
    while answer != 'no':
        print('Want another question? (yes/no)')
        answer = input()
        if (answer == 'no'):
            print('Well, bye! Lazy...')
        elif (answer == 'yes'):
            q = generate_question(words=words_list, answers=answers)
            os.system('clear')
            print('Word: {}'.format(q['word']))
            print()
            print('a) {}'.format(q['a']))
            print('b) {}'.format(q['b']))
            print('c) {}'.format(q['c']))
            print('d) {}'.format(q['d']))
            print()
            print('You can type only --> a, b, c, d')
            ans = input()
            if (q['{}'.format(ans)] == q['right_answ']):
                print('OK! It\'s right!')
            else:
                print('I\'m sorry, but it\'s not')
        else:
            print('Just say "yes" or "no"!')



# Генерация вопроса
def generate_question(words, answers):
    # Случайное слово из общего списка
    index = random.randint(0, len(words))
    word = words[index]

    # Создаем лист трех случайных чисел 
    # Проверяем, чтобы они все были разные
    a_indexes = []
    for i in range(0, 3):
            a_indexes.append(random.randint(0, len(answers)))
    
    # Добавляем в список индексов ответов индекс текущего слова
    # Это нужно, чтобы другие варианты не повторяли правильный ответ
    a_indexes.append(index)

    # Проверяем на уникальность лист индексов
    # Все четыре индекса должны быть разные
    while len(numpy.unique(a_indexes)) != len(a_indexes):
        for i in range(0, 3):
            a_indexes.append(random.randint(0, len(answers)))
    
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


# Функция считывания содержимого файла
def read_from_file():
    # Лист из всех определений слов 
    answers = []

    # Лист слов
    words = []

    with codecs.open('TOEFLWordBase.csv', 'r', encoding='utf-8', errors='ignore') as row_words:

        # Считываем содержимое файла в итерируемый объект
        reader = csv.reader(row_words)

        for row in reader:
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
    return {'answers': answers, 'words': words}
