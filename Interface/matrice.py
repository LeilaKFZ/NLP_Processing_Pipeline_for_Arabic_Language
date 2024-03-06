import json
from collections import Counter

# Définir le chemin du fichier contenant le corpus nettoyé
fichier_corpus = "./Datas/train_file.txt"

# Fonction pour lire et charger le corpus nettoyé
def charger_corpus(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        corpus_nettoye = [ligne.strip().split() for ligne in f]
    return corpus_nettoye

# Charger le corpus nettoyé depuis le fichier
corpus_nettoye = charger_corpus(fichier_corpus)

# Créer la matrice de génération

next_words = {}
for sentence in corpus_nettoye:
    for i, word in enumerate(sentence[:-1]):
        next_word = sentence[i + 1]
        if word in next_words:
            next_words[word].append(next_word)
        else:
            next_words[word] = [next_word]

# Compter la fréquence de chaque next word et la fréquence de chaque mot distinct
mot_freq = Counter()
next_word_freq = {}
for word, next_word_list in next_words.items():
    next_word_freq[word] = Counter(next_word_list)
    mot_freq[word] += 1

# Créer la structure de données JSON
json_data = []
for word, freq in mot_freq.items():
    json_data.append({
        'word': word,
        'frequency': freq,
        'next_words': [{'next_word': nw, 'frequency': next_word_freq[word][nw]} for nw in next_word_freq[word]]
    })

# Écrire la structure de données JSON dans un fichier
with open('matrice_generation.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("La matrice de génération a été créée et enregistrée dans le fichier `matrice_generation.json`.")
