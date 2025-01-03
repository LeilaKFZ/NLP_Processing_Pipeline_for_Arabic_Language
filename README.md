# NLP Processing Pipeline for  Arabic Language
## Interactive Arabic Text Suggestion System

This project presents an "interactive Arabic text suggestion system" built on a meticulously preprocessed corpus. The preprocessing steps include:

1. Tokenization using:
   - Utilizes "nltk" to split text into individual tokens.
2. Cleaning:
   - Removes punctuation marks, special characters, and stop words.
3. Dictionary Check:
   - Ensures that tokens are valid Arabic words by verifying them against an Arabic dictionary.
4. Lemmatization:
   - Uses "qalsadi lemmatizer" to reduce words to their canonical form. 
5. Stemming:
   - Applies the "farasa stemmer" to extract word roots for precise morphological analysis.
8. Named Entity Recognition (NER):
   - Leverages  "farasa ner" to dentify key entities such as proper names ans places.

## Diagram of the Processing Pipeline:
![TALNNN](https://github.com/user-attachments/assets/368154f7-6aa4-4104-a566-7ee2ea2756dd)

## System Output
 - The processed corpus is saved as a JSON file.
 - This JSON file is then used in the Streamlit interface to generate next-word suggestions interactively.

## Technologies Used:
    - NLTK
    - Qalsadi Lemmatizer
    - Farasa Tools (Stemmer and NER)
    - Streamlit

