# pip install tk  genanki

import csv
from pathlib import Path

import genanki

new_words = Path().home()/'Library/Mobile Documents/com~apple~CloudDocs/ANKI/Saved translations - Saved translations.csv'
anki_folder = Path().home()/'Library/Mobile Documents/com~apple~CloudDocs/ANKI'

words_file = Path().home()/'Library/Mobile Documents/com~apple~CloudDocs/ANKI/The Oxford 3000.txt'

model_id = 1194120293  # random.randrange(1 << 30, 1 << 31)
# print(model_id)

deck_id = 1553030151  # random.randrange(1 << 30, 1 << 31)
# print(deck_id)

my_model = genanki.Model(model_id,
                         'Oxford_3000',
                         fields=[
                             {'name': 'Front'},
                             {'name': 'Back'}
                         ],
                         templates=[
                             {
                                 'name': 'Card type 1',
                                 'qfmt': '{{Question}}',
                                 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                             },
                         ])

my_deck = genanki.Deck(deck_id, "Oxford_3000")


def add_note_from_csv():
    with open(new_words, 'r') as csv_file:
        words = csv.reader(csv_file)
        for line in words:
            my_note = genanki.Note(
                model=my_model,
                fields=[f'{line[2].lower()}', f'{line[3].lower()}'])
            my_deck.add_note(my_note)
            print(line)


def add_note_txt_file():
    with open(words_file, 'r') as input_file:
        lines = input_file.readlines()
        for i in range(6, len(lines)):
            if not lines[i].isspace():
                word = lines[i].strip().split()[0]
                my_note = genanki.Note(
                    model=my_model,
                    fields=[f'{word}', f''])
                my_deck.add_note(my_note)


add_note_txt_file()

anki_questions_file = f'{anki_folder}/anki_question_6.apkg'
genanki.Package(my_deck).write_to_file(anki_questions_file)
