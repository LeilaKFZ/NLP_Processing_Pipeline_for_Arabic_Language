import streamlit as st
import json

with open('../Datas/arabic_matrix.json', 'r', encoding='utf-8') as f:
    word_data = json.load(f)


# Fct to get three TOP next words
def get_next_words(word):
    if word in word_data:
        # Extraire les mots suivants de "next_words" et retourner les TROIS PREMIERS
        return list(word_data[word]["next_words"].keys())[:3]
    else:
        return []

## add some style #####
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
            color: #333333;
            font-family: 'Arial', sans-serif;
            direction: rtl;
            text-align: right;
        }
        .title {
            color: #2a9d8f;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #264653;
            font-size: 20px;
            margin-bottom: 20px;
        }
        .current-sequence {
            background-color: #e9ecef;
            padding: 10px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            color: #333333;
            text-align: right;
        }
        .word-button {
            background-color: #2a9d8f;
            color: white;
            border: none;
            padding: 8px 16px;
            margin: 5px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .word-button:hover {
            background-color: #21867a;
        }
    </style>
""", unsafe_allow_html=True)

# Interface --Streamlit
st.markdown("<h1 class='title'>اقتراح الكلمات التالية</h1>", unsafe_allow_html=True)

# trace of seq
if "current_word" not in st.session_state:
    st.session_state.current_word = ""
if "sequence" not in st.session_state:
    st.session_state.sequence = []

# First word to begin with
if not st.session_state.current_word:
    input_word = st.text_input("ابدأ بكلمة", placeholder="ادخل الكلمة الأولى")
    if input_word:
        st.session_state.current_word = input_word
        st.session_state.sequence.append(input_word)

# print actual seq
if st.session_state.sequence:
    st.markdown("### الجملة الحالية:")
    st.markdown(f"<div class='current-sequence'>{' '.join(st.session_state.sequence)}</div>", unsafe_allow_html=True)

# next word proposition
if st.session_state.current_word:
    next_words = get_next_words(st.session_state.current_word)
    if next_words:
        st.markdown("### كون جملتك:")
        # Ajouter des boutons pour chaque mot suivant
        for next_word in next_words:
            if st.button(next_word, key=next_word):  # Clé unique pour chaque bouton
                # Mettre à jour la séquence et le mot courant
                st.session_state.sequence.append(next_word)
                st.session_state.current_word = next_word
    else:
        st.write("لا توجد كلمات تالية متاحة.")
