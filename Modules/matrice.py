import json
from collections import defaultdict
import os


def create_word_cooccurrence_json(corpus_dir, vocabulary_file, output_json):
    """
    Reads text files from a corpus directory, checks words against vocabulary,
    and creates a JSON file with word counts and co-occurrences, SORTED by next word occurrence count.

    Args:
        corpus_dir (str): Path to the directory containing text files.
        vocabulary_file (str): Path to the file containing vocabulary words.
        output_json (str): Path to the output JSON file.
    """
    # Load vocabulary into a set for faster lookup
    with open(vocabulary_file, 'r', encoding='utf-8') as f:
        vocabulary = set(line.strip() for line in f)

    # Initialization
    word_data = defaultdict(lambda: {"count": 0, "next_words": defaultdict(int)})

    # Read corpus -train- files
    for filename in os.listdir(corpus_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(corpus_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                # Read the text file and split into words
                for line in f:
                    words = line.strip().split()
                    for i, word in enumerate(words):
                        # Check if word is in vocabulary
                        if word.lower() in vocabulary:
                            word_data[word.lower()]["count"] += 1
                            # Check for next word (if not the last word)
                            if i < len(words) - 1:
                                next_word = words[i+1].lower()
                                if next_word in vocabulary:
                                    word_data[word.lower()]["next_words"][next_word] += 1

    # Sort next_words according to descending order
    total_word_count = 0
    for word, data in word_data.items():
        total_word_count += data["count"]
        #data["next_words"] = dict(sorted(data["next_words"].items(), key=lambda item: item[1], reverse=True))
        data["next_words"] = dict(sorted(data["next_words"].items(), key=lambda item: item[1], reverse=True)[:3])

    #s ave
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(word_data, f, indent=4)


corpus_dir = "../train_tk"
vocabulary_file = "../Datas/vocabulary.txt"
output_json = "../Datas/matrice.json"

create_word_cooccurrence_json(corpus_dir, vocabulary_file, output_json)
