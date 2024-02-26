######## Les deux codes sont a developpe, ce n'est que le premier essai
###############

# Alipy (il gere le fichier train_file et met le resultat dans  final_train_file)
import alipy

# Définir le fichier d'entrée et de sortie
fichier_entree = "./Datas/train_file.txt"
fichier_sortie = "./Datas/final_train_file.txt"

# Ouvrir le fichier d'entrée en lecture
with open(fichier_entree, "r", encoding="utf-8") as f_in:
    texte_arabe = f_in.read()

# Tokeniser le texte
tokens = TOKENIZER(texte_arabe)

# Lemmatiser les tokens
lemmes = [token.lemma for token in tokens]

# Ouvrir le fichier de sortie en écriture
with open(fichier_sortie, "w", encoding="utf-8") as f_out:
    for token, lemme in zip(tokens, lemmes):
        # Écrire le token et son lemme dans le fichier de sortie
        f_out.write(f"{token.text} {lemme}\n")

print("Le traitement est terminé. Le résultat est dans le fichier `final_train_file.txt`.")

######################################
## Alyahmor (gere qu'un petit exemple pour le mom)

import alyahmor as aly

# Définir le fichier d'entrée et de sortie
fichier_entree = "./Datas/train_file.txt"
fichier_sortie = "./Datas/final_train_file.txt"

# Charger le modèle de langage
model = aly.load_model("ar")  # "ar" pour l'arabe

# Ouvrir le fichier d'entrée en lecture
with open(fichier_entree, "r", encoding="utf-8") as f_in:
    texte_arabe = f_in.read()

# Tokeniser le texte
tokens = aly.tokenize(texte_arabe)

# Lemmatiser les tokens
lemmes = [token.lemma for token in tokens]

# Ouvrir le fichier de sortie en écriture
with open(fichier_sortie, "w", encoding="utf-8") as f_out:
    for token, lemme in zip(tokens, lemmes):
        # Écrire le token et son lemme dans le fichier de sortie
        f_out.write(f"{token.text} {lemme}\n")

print("Le traitement est terminé. Le résultat est dans le fichier `final_train_file.txt`.")