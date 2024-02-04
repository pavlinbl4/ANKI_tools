 # pip install tk  genanki

import random
import genanki
from pathlib import Path
import os

new_words = f'{Path().home()}/Downloads/Saved translations - Saved translations.csv'
anki_folder = f"{Path().home()}/Documents/ANKI"

os.makedirs(anki_folder, exist_ok=True)

# model_id = random.randrange(1 << 30, 1 << 31)
model_id = 2137747653
print(f"{model_id = }")

deck_id = random.randrange(1 << 30, 1 << 31)
deck_id = 1780842558
print(f"{deck_id = }")

my_model = genanki.Model(model_id,
                         'Python generated cards',
                         fields=[
                             {'name': 'Front'},
                             {'name': 'Back'},
                             {'name': 'Grammar'},
                             {'name': 'Definition'},
                             {'name':'Sound'},
                             {'name':'Eng'},
                             {'name':'Synonyms'},
                             {'name':'Transcription'},
                             {'name':'Image'}
                         ],
                         templates=[
                             {
                                 'name': 'Card type 1',
                                 'qfmt': '{{Question}}',
                                 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                             },
                         ])

my_deck = genanki.Deck(deck_id, "Knowledge with Python")



note = genanki.Note(
  model=my_model,
  fields=['Front text!', 'Back text!', 'Grammar text!', 'Definition text', 'Sound text', 'Eng text', 'Synonyms text', 'Transcription text', 'Image text'])

my_deck.add_note(note)


anki_questions_file = f'{anki_folder}/anki_question_python.apkg'
genanki.Package(my_deck).write_to_file(anki_questions_file)
