# NLP Processing Pipeline for  Arabic Language
## Generate next words from a small pre-processed arabic corpus

### This project presents an "interactive Arabic text suggestion system" built on a meticulously preprocessed corpus. The preprocessing steps include:

1. Tokenization using "nltk": Splitting text into tokens.
2. Removing all punctuation marks, special characters, and stop words from the corpus.
3. Check if the tokens are included in the Arabic dictionary.
4. Lemmatization using "qalsadi lemmatizer": Reducing words to their canonical form. 
    - If it returns true, the token is identified as an arabic word.
5. Stemming using "farasa stemmer": Extracting word roots for precise morphological analysis.
    - If it returns true, the roots are checked against the dictionary.
6. Named Entity Recognition (NER) using  "farasa ner": Identifying key entities such as proper names,places, etc.

### Here is a detailed diagram of the processing pipeline:
![TALNNN](https://github.com/user-attachments/assets/368154f7-6aa4-4104-a566-7ee2ea2756dd)

Once processing is completed, the generated JSON file containing the next words is used in the Streamlit interface.


