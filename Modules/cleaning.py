import re
import arabic_reshaper
from nltk.corpus import stopwords

# Définir le chemin vers le fichier de stop words
STOP_WORDS_FILE = "./Datas/stop_arabic.txt"

# Charger les stop words
with open(STOP_WORDS_FILE, "r", encoding="utf-8") as f:
    stop_words = set(f.read().splitlines())

# Fonction pour nettoyer le texte
def clean_text(text):
    # Supprimer ponctuations et caractères spéciaux
    text = re.sub(r"[^\w\s]", " ", text)
    # Supprimer les stop words
    text = " ".join(word for word in text.split() if word not in stop_words)
    # Supprimer les numéros
    text = re.sub(r"\d+", "", text)
    # Normaliser le texte arabe
    text = arabic_reshaper.reshape(text)
    return text

# Ouvrir le fichier en mode lecture et écriture
with open("./Datas/train_file.txt", "r+", encoding="utf-8") as f:
    # Lire le contenu du fichier
    text = f.read()
    # Nettoyer le texte
    cleaned_text = clean_text(text)
    # Retourner au début du fichier pour écrire le texte nettoyé
    f.seek(0)
    # Écrire le texte nettoyé dans le fichier en écrasant le contenu initial
    f.write(cleaned_text)
    f.truncate()

print("Le fichier train_file.txt a été nettoyé avec succès.")
