# pip install tk  genanki

import random
import genanki
import csv
from pathlib import Path
import os

new_words = f'{Path().home()}/Downloads/Saved translations - Saved translations.csv'
anki_folder = f"{Path().home()}/Documents/ANKI"

os.makedirs(anki_folder, exist_ok=True)

model_id = random.randrange(1 << 30, 1 << 31)
print(model_id)

deck_id = random.randrange(1 << 30, 1 << 31)
print(deck_id)

my_model = genanki.Model(model_id,
                         'My English cards',
                         fields=[
                             {'name': 'Front'},
                             {'name': 'Back'},
                             # {'name': 'Grammar'},
                             # {'name': 'Definition'},
                             # {'name':'Sound'},
                             # {'name':'Eng'},
                             # {'name':'Synonyms'},
                             # {'name':'Transcription'},
                             # {'name':'Image'}
                         ],
                         templates=[
                             {
                                 'name': 'Card type 1',
                                 'qfmt': '{{Question}}',
                                 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                             },
                         ])

my_deck = genanki.Deck(deck_id, "Knowledge")

with open(new_words, 'r') as csv_file:
    words = csv.reader(csv_file)
    for line in words:
        my_note = genanki.Note(
            model=my_model,
            fields=[f'{line[2].lower()}', f'{line[3].lower()}'])

        my_deck.add_note(my_note)

        print(line)

anki_questions_file = f'{anki_folder}/anki_question.apkg'
genanki.Package(my_deck).write_to_file(anki_questions_file)
