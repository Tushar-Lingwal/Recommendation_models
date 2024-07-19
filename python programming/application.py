import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

songs = pd.read_csv("songdata.csv")
root = tk.Tk()
root.title("Song Recommendation System")

frame = ttk.Frame(root, padding="100")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Select a Song:")
label.grid(row=0, column=0, padx=5, pady=5)

song_names = songs['song'].tolist()
selected_song = tk.StringVar()
dropdown = ttk.Combobox(frame, textvariable=selected_song)
dropdown['values'] = song_names
dropdown.grid(row=0, column=1, padx=5, pady=5)
button = ttk.Button(frame, text="Get Recommendations")
button.grid(row=0, column=2, padx=5, pady=5)

result_frame = ttk.Frame(root, padding="10")
result_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()