from farasa.ner import FarasaNamedEntityRecognizer
import os

# initialize NER
ner = FarasaNamedEntityRecognizer()

file_stemmes = os.path.join("..", "Datas", "stem_not.txt")
with open(file_stemmes, "r", encoding="utf-8") as file_stemmes:
    mots = file_stemmes.read().splitlines()

for mot in mots:
    # Recognize named entities
    entities = ner.recognize(mot)
    #print(entities)

    if "/O" in entities:
        #print(f"{mot}not recognized")
        with open("../Datas/ner_not.txt", "a", encoding='utf-8') as f_novocab:  f_novocab.write(mot + "\n")

    else:
        #print(f"{mot}it is recognize")
        with open("../Datas/YES_ner.txt", "a", encoding='utf-8') as f_vocab:  f_vocab.write(mot + "\n")
