import os
import re
import nltk

# Définir le chemin du dossier
dossier = "../train"

# Charger le modèle de tokenisation arabe
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|\$[\w\-]+\$')

# Charger les stop words de NLTK
nltk_stop_words = set(nltk.corpus.stopwords.words("arabic"))

# Charger les stop words à partir du fichier texte
with open('../Datas/stop_arabic.txt', 'r', encoding='utf-8') as f:
    fichier_stop_words = set(f.read().splitlines())

# Concaténer les stop words de NLTK avec ceux du fichier texte
stop_words = nltk_stop_words.union(fichier_stop_words)

# Créer le dossier "train_tk" s'il n'existe pas
if not os.path.exists(os.path.join(dossier, "train_tk")):
    os.mkdir(os.path.join(dossier, "train_tk"))

# Itérer sur les fichiers du dossier
for fichier in os.listdir(dossier):
    # Vérifier si c'est un fichier .txt
    if fichier.endswith(".txt"):
        # Ouvrir le fichier en mode lecture
        with open(os.path.join(dossier, fichier), "r+", encoding="utf-8") as f:
            # Lire le contenu du fichier ligne par ligne
            lignes = f.readlines()

        # Traiter chaque ligne
        lignes_tokenisees = []
        for ligne in lignes:
            # Nettoyer la ligne
            ligne = re.sub(r'\W+', ' ', ligne)
            ligne = re.sub(r'[0-9]+', ' ', ligne)

            # Tokenizer la ligne
            tokens = nltk.word_tokenize(ligne)

            # Filtrer les stop words
            tokens = [token for token in tokens if token not in stop_words]

            # Ajouter les tokens à la liste
            lignes_tokenisees.append(" ".join(tokens))

        # Écrire les lignes tokenisées dans un fichier du dossier "train_tk"
        with open(os.path.join(dossier, "train_tk", fichier), "w+", encoding="utf-8") as f:
            f.write("\n".join(lignes_tokenisees))

print("Traitement terminé.")
