import tkinter as tk
import json

import json

with open('../Datas/matrice_arabe.json',encoding='utf-8') as f:
    data = json.load(f)


def filter_suggestions(mot_tape):
    suggestions = []
    for mot, word_data in data.items():
        if mot.lower() == mot_tape:  # Check for exact match (case-insensitive)
            next_words = word_data['next_words']
            for next_word, occurrence in next_words.items():  # Iterate through next_words
                suggestions.append((next_word, occurrence))  # Add next_word and occurrence
            break  # Stop iterating once a match is found
    return suggestions[:3]  # Limit to 5 suggestions



def update_suggestions(event):
    mot_tape = entry.get()
    suggestions_list.delete(0, tk.END)
    for mot, _ in filter_suggestions(mot_tape):
        suggestions_list.insert(tk.END, mot)

root = tk.Tk()
root.title('Arabic Text Generator (Tkinter)')

label = tk.Label(root, text='Enter Arabic word:')
label.pack()

entry = tk.Entry(root)
entry.bind('<KeyRelease>', update_suggestions)
entry.pack()

suggestions_list = tk.Listbox(root, width=30)
suggestions_list.pack()

root.mainloop()
