import os
import re

# open both files
with open("../Datas/dictionary.txt", "r", encoding='utf-8') as f_dict:
    dict_start = set(f_dict.read().splitlines())
with open("../Datas/vocabulary.txt", "w", encoding='utf-8') as f_vocab:
    pass
with open("../Datas/non_dict.txt", "w", encoding='utf-8') as f_not:
    pass

dossier = "../train_tk"

###### fct
def analyse_fichier(fichier):
    with open(os.path.join(dossier, fichier), "r", encoding='utf-8') as f:
        texte = f.read()
    # mots = re.findall(r"\w+", texte)
    mots = texte.split()
    for mot in mots:
        if mot in dict_start:
            # Ecrire le mot dans le fichier vocabulaire
            with open("../Datas/vocabulary.txt", "a", encoding='utf-8') as f_vocab:
                f_vocab.write(mot + "\n")
        else:
            # Ecrire le mot dans le fichier non-vocabulaire
            with open("../Datas/non_dict.txt", "a", encoding='utf-8') as f_not:
                f_not.write(mot + "\n")

##### Begine the analyse
for fichier in os.listdir(dossier):
    if fichier.endswith(".txt"):
        analyse_fichier(fichier)
