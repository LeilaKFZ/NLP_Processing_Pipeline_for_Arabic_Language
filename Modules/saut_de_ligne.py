import os


def split_text_by_punctuation(text):
    """
    Splits a text into sentences based on punctuation marks.

    Args:
        text: The text to be split.

    Returns:
        A list of sentences.
    """
    punctuation = [".", "!", "؟", "،"]
    sentences = []
    current_sentence = ""
    for char in text:
        if char in punctuation:
            sentences.append(current_sentence.strip())
            current_sentence = ""
        else:
            current_sentence += char
    # Add the last sentence if it exists
    if current_sentence:
        sentences.append(current_sentence.strip())
    return sentences


# Get the current working directory
cwd = os.getcwd()

# Change directory to "jeu"
os.chdir("../train")

# Iterate through all files in the directory
for filename in os.listdir():
    # Check if it's a .txt file
    if filename.endswith(".txt"):
        # Read the file contents
        with open(filename, "r", encoding='utf-8') as f:
            text = f.read()

        # Split the text into sentences
        sentences = split_text_by_punctuation(text)

        # Write the sentences back to the file
        with open(filename, "w", encoding='utf-8') as f:
            for sentence in sentences:
                f.write(sentence + "\n")

# Change directory back to the original directory
os.chdir(cwd)

print("Traitement terminé.")
