import json
import os

def tester_modele(corpus_dir, vocabulary_file, matrice_json_file, resultat_file):
    """
    Tests the word prediction model on the test corpus.
    Calculates the total score (+1 for correct predictions, -1 for incorrect).

    Args:
        corpus_dir (str): Path to the directory containing test text files.
        vocabulary_file (str): Path to the file containing vocabulary words.
        matrice_json_file (str): Path to the JSON file containing the word co-occurrence matrix.
        resultat_file (str): Path to the file where the test results will be saved.
    """

    # Load vocabulary from file
    with open(vocabulary_file, 'r', encoding='utf-8') as f:
        vocabulary = set(line.strip() for line in f)

    # Load word co-occurrence matrix from JSON file
    with open(matrice_json_file, 'r', encoding='utf-8') as f:
        matrice_json = json.load(f)

    # Initialize score counter
    total_score = 0

    # Open file to write results
    with open(resultat_file, 'w', encoding='utf-8') as f_resultat:
        f_resultat.write("## Test du modèle sur le corpus de test\n\n")

        # Loop through files in the corpus directory
        for filename in os.listdir(corpus_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(corpus_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    # Read the text file line by line
                    for line in f:
                        words = line.strip().split()

                        # Process each word in the line
                        for i, word in enumerate(words):
                            # Check if word is in vocabulary
                            if word in vocabulary:
                                # Check for next word (if not the last word)
                                if i < len(words) - 1:
                                    next_word = words[i + 1]


                                    # Check if next word is in vocabulary
                                    if next_word in vocabulary:
                                        # Check if next word is among the possible next words in the matrix
                                        next_words_matrice = matrice_json[word.lower()]["next_words"]
                                        if next_word in next_words_matrice:
                                            # Prediction is correct
                                            total_score += 1
                                            f_resultat.write(f"{word} -> {next_word}: Correct (+1)\n")
                                        else:
                                            # Prediction is incorrect
                                            total_score -= 1
                                            f_resultat.write(f"{word} -> {next_word}: Incorrect (-1)\n")
                                    else:
                                        # Next word not in vocabulary
                                        f_resultat.write(f"{word} -> {next_word}: Next word not in vocabulary\n")
                            else:
                                # Word not in vocabulary
                                f_resultat.write(f"{word} not in vocabulary\n")

    # Print and write the total score
    print(f"\n**Score total : {total_score}**")
    f_resultat.write(f"\n**Score total : {total_score}**")


# Replace with your actual directory paths and file names
corpus_dir = "../test_tk"
vocabulary_file = "../Datas/vocabulary.txt"
matrice_json_file = "../Datas/matrice_arabe.json"
resultat_file = "../Datas/resultat_test.txt"

tester_modele(corpus_dir, vocabulary_file, matrice_json_file, resultat_file)
