from farasa.stemmer import FarasaStemmer
import os

stemmer = FarasaStemmer()

# Définir les chemins d'accès aux fichiers
fichier_lemmes = os.path.join("..", "Datas", "lem_not.txt")
fichier_dictionnaire = os.path.join("..", "Datas", "dictionary.txt")

# Ouvrir le fichier lem_not.txt "les mots non lemmatisés"
with open(fichier_lemmes, "r", encoding='utf-8') as f_non_lem:
    mots = f_non_lem.read().splitlines()

# Ouvrir le fichier dictionary.txt
with open(fichier_dictionnaire, "r", encoding='utf-8') as f_dict:
    dict = set(f_dict.read().splitlines())

# Stemmer les mots et les ajouter au dictionnaire
for mot in mots:
    stem = stemmer.stem(mot)

# Itérer sur les mots et les classer
    if stem in dict:
        # Ecrire le mot dans le fichier vocabulaire
        with open("../Datas/vocabulary.txt", "a", encoding='utf-8') as f_vocab:
                    f_vocab.write(mot + "\n")
    else:
        # Ecrire le mot dans le fichier non-vocabulaire
        with open("../Datas/stem_not.txt", "a", encoding='utf-8') as f_not:
                    f_not.write(mot + "\n")
