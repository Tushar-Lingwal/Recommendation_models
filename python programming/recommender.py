import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, data_path):
        self.songs = pd.read_csv(data_path)
        self.songs = self.songs.sample(n=10000).drop('link', axis=1).reset_index(drop=True)
        self.songs['text'] = self.songs['text'].str.replace(r'\n', '')
        self.tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.songs['text'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        self.similarities = {}
        for i in range(len(self.cosine_sim)):
            similar_indices = self.cosine_sim[i].argsort()[:-50:-1]
            self.similarities[self.songs['song'].iloc[i]] = [
                (self.cosine_sim[i][x], self.songs['song'][x], self.songs['artist'][x]) for x in similar_indices][1:]

    def recommend(self, song, number_songs):
        recom_song = self.similarities.get(song, [])[:number_songs]
        return recom_song
