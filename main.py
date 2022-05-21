# pip install tk  genanki

import random
import genanki
import csv

new_words = '/Volumes/big4photo/Documents/ANKI/Saved translations - Saved translations.csv'
anki_folder = "/Volumes/big4photo/Documents/ANKI"

model_id = random.randrange(1 << 30, 1 << 31)
print(model_id)

deck_id = random.randrange(1 << 30, 1 << 31)
print(deck_id)

my_model = genanki.Model(model_id,
                         'Knowledge',
                         fields=[
                             {'name': 'Question'},
                             {'name': 'Answer'},
                         ],
                         templates=[
                             {
                                 'name': 'Card type 1',
                                 'qfmt': '{{Question}}',
                                 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                             },
                         ])

my_deck = genanki.Deck(deck_id, "Knowledge")

with open(new_words,'r') as csv_file:
    words = csv.reader(csv_file)
    for line in words:
        my_note = genanki.Note(
            model=my_model,
            fields=[f'{line[2].lower()}', f'{line[3].lower()}'])

        my_deck.add_note(my_note)

        print(line)










anki_questions_file = f'{anki_folder}/anki_question.apkg'
genanki.Package(my_deck).write_to_file(anki_questions_file)
