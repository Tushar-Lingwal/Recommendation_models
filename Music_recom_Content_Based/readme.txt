Content-Based Song Recommendation System
Overview
The Content-Based Song Recommendation System is a Python application that utilizes a content-based filtering approach to recommend songs. 
The application features a graphical user interface (GUI) built using Tkinter, which allows users to select a song and receive recommendations 
based on the textual content of song lyrics. The system leverages the TF-IDF vectorizer and cosine similarity to compute recommendations.

Features
- Welcome Screen: An initial screen with a welcome message and options to enter the recommendation system or exit the application.
- Main Interface: A user-friendly interface where users can:
    Select a song from a dropdown list.
    Filter the dropdown list by artist.
    Get song recommendations based on the selected song.
    View recommendations in a scrollable frame.
- Content-Based Filtering: The recommendation engine uses TF-IDF vectorization and cosine similarity to suggest similar songs based on lyrics.
Installation
Prerequisites
-Python 3.6+
-pandas
-scikit-learn
-tkinter (usually included with Python installations)
-Pillow (for image handling)
