# Content-Based Song Recommendation System🎵🎶🎵
## Overview
The Content-Based Song Recommendation System is a Python application that utilizes a content-based filtering approach to recommend songs. The application features a graphical user interface (GUI) built using Tkinter, which allows users to select a song and receive recommendations based on the textual content of song lyrics. The system leverages the TF-IDF vectorizer and cosine similarity to compute recommendations.

## Features
- Welcome Screen: An initial screen with a welcome message and options to enter the recommendation system or exit the application.
- Main Interface: A user-friendly interface where users can:
    - Select a song from a dropdown list.
    - Filter the dropdown list by artist.
    - Get song recommendations based on the selected song.
    - View recommendations in a scrollable frame.
- Content-Based Filtering: The recommendation engine uses TF-IDF vectorization and cosine similarity to suggest similar songs based on lyrics.

## Installation
- Prerequisites
- Python 3.6+
- pandas
- scikit-learn
- tkinter (usually included with Python installations)
- Pillow (for image handling)

## preview of the window 

![image](https://github.com/user-attachments/assets/5f78316e-72d1-4ea1-9125-3ab799db2c9f)

![image](https://github.com/user-attachments/assets/66c52b40-cb60-44ed-9acc-b4ff09f87ceb)

## Usage
Running the Application
1. Run the welcome (main.py) Screen:

![image](https://github.com/user-attachments/assets/8bbf4d52-7c66-41f3-8a7b-cfca1e0d7336)

2. Interacting with the Application:
    - On the welcome screen, click "Enter" to proceed to the main interface or "Exit" to close the application.
    - On the main interface:
        -Select a song from the dropdown list.
        -Optionally filter the dropdown list by selecting an artist and clicking "Filter by Artist".
        -Click "Get Recommendations" to view recommended songs.
    -The recommendations are displayed in a scrollable frame below the dropdown list.

## File Structure
- main.py: Main script containing the application interface and logic.
- recommender.py: Module containing the ContentBasedRecommender class and recommendation logic.
- songdata.csv: CSV file containing song data (ensure this file is in the project directory).
- background.png: Background image for the GUI (optional, ensure this file is in the project directory).
