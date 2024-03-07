import random
import os
import shutil

# Définir le chemin du dossier source
dossier_source = "C:\\Users\\HP\\Desktop\\fatima zohra\\Sports"

# Définir le nombre de fichiers pour chaque ensemble
taille_train = 6000
taille_test = 500

# Définir les chemins des dossiers train et test
dossier_train = "C:\\Users\\HP\\Desktop\\fatima zohra\\taln\\train"
dossier_test = "C:\\Users\\HP\\Desktop\\fatima zohra\\taln\\test"

# Mélanger aléatoirement les fichiers
fichiers = os.listdir(dossier_source)
random.shuffle(fichiers)

# Créer les dossiers s'ils n'existent pas déjà
os.makedirs(dossier_train, exist_ok=True)
os.makedirs(dossier_test, exist_ok=True)

# Déplacer les fichiers
for i, fichier in enumerate(fichiers):
    if i < taille_train:
        shutil.move(os.path.join(dossier_source, fichier), dossier_train)
    else:
        shutil.move(os.path.join(dossier_source, fichier), dossier_test)

# Afficher un message de confirmation
print("Fichiers divisés avec succès !")
