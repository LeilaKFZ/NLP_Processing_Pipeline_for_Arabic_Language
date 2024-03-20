import qalsadi.lemmatizer

# Ouvrir le fichier non_dict.txt "les mots non trouvés dans le dict"
with open("../Datas/non_dict.txt", "r", encoding='utf-8') as f_non_dict:
    mots = f_non_dict.read().splitlines()

# Initialiser le lemmatiseur Qalsadi
lemmer = qalsadi.lemmatizer.Lemmatizer()

# Itérer sur les mots
for mot in mots:
    # Lemmatiser le mot
    lemmas = lemmer.lemmatize_text(mot)
    # Si la liste de lemmes est vide, le mot n'est pas correctement lemmatisé
    if not lemmas:
        with open("../Datas/lem_not.txt", "a", encoding='utf-8') as f_chofi:
            f_chofi.write(mot + "\n")
    else:
        # Si la liste de lemmes ne contient que le mot lui-même, c'est aussi un échec
        if len(lemmas) == 1 and lemmas[0] == mot:
            with open("../Datas/lem_not.txt", "a", encoding='utf-8') as f_chofi:
                f_chofi.write(mot + "\n")
        else:
            # Ecrire le mot original  dans le fichier correct
            with open("../Datas/vocabulary.txt", "a", encoding='utf-8') as f_correct:
                f_correct.write(mot + "\n")

