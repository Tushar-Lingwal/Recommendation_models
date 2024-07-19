import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
songs = pd.read_csv('songdata.csv')

songs = songs.sample(n=10000).drop('link', axis=1).reset_index(drop=True)
songs['text'] = songs['text'].str.replace(r'\n', '')
tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
tfidf_matrix = tfidf.fit_transform(songs['text'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

similarities = {}
for i in range(len(cosine_sim)):
    similar_indices = cosine_sim[i].argsort()[:-50:-1]
    similarities[songs['song'].iloc[i]] = [(cosine_sim[i][x], songs['song'][x], songs['artist'][x]) for x in similar_indices][1:]
class ContentBasedRecommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    def recommend(self, song, number_songs):
        recom_song = self.matrix_similar[song][:number_songs]
        return recom_song
recommendations = ContentBasedRecommender(similarities)

root = tk.Tk()
root.title("Song Recommendation System")

frame = ttk.Frame(root, padding="10")
frame.grid(row=10, column=10, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Select a Song:")
label.grid(row=0, column=0, padx=5, pady=5)

song_names = songs['song'].tolist()
selected_song = tk.StringVar()
dropdown = ttk.Combobox(frame, textvariable=selected_song)
dropdown['values'] = song_names
dropdown.grid(row=0, column=1, padx=5, pady=5)

def show_recommendations():
    song = selected_song.get()
    number_songs = 10
    recom_song = recommendations.recommend(song, number_songs)
    
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    ttk.Label(result_frame, text=f"Recommended songs for '{song}':").grid(row=0, column=0, padx=5, pady=5)
    for i, (score, song_name, artist) in enumerate(recom_song):
        ttk.Label(result_frame, text=f"{i+1}. {song_name} by {artist} (Score: {round(score, 3)})").grid(row=i+1, column=0, padx=5, pady=2)

button = ttk.Button(frame, text="Get Recommendations", command=show_recommendations)
button.grid(row=0, column=2, padx=5, pady=5)

result_frame = ttk.Frame(root, padding="10")
result_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()
