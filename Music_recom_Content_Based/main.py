import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from recommender import ContentBasedRecommender

# Initialize the recommender with the path to your song data CSV
recommendations = ContentBasedRecommender('songdata.csv')

def open_recommendation_system():
    welcome_window.destroy()
    main_interface()

def exit_application():
    welcome_window.destroy()

def main_interface():
    root = tk.Tk()
    root.title("Song Recommendation System")
    root.geometry("800x600")  # Fixed large size for the main window

    # Load the background image
    background_image = Image.open("images/istockphoto-1076840920-612x612.jpg")
    background_image = background_image.resize((800, 600), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(background_image)

    # Create a canvas to hold the background image
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Create a frame for the UI elements
    ui_frame = ttk.Frame(root, padding="20", style='TFrame')
    ui_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)  # Centered in the window

    heading_label = ttk.Label(root, text="CONTENT BASED FILTERING", font=("Helvetica", 20, "bold"))
    heading_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Create and place the label, dropdown, and button in the ui_frame
    label = ttk.Label(ui_frame, text="Select a Song:")
    label.grid(row=1, column=0, padx=5, pady=5)

    song_names = recommendations.songs['song'].tolist()
    selected_song = tk.StringVar()
    dropdown = ttk.Combobox(ui_frame, textvariable=selected_song)
    dropdown['values'] = song_names
    dropdown.grid(row=1, column=1, padx=5, pady=5)
    #### added changer -------------------------------------------------------------- here
    label2 = ttk.Label(ui_frame, text="Select an ARTIST:")
    label2.grid(row=0, column=0, padx=5, pady=5)
    artist_names = recommendations.songs['artist'].unique().tolist()
    artist_filter = tk.StringVar()
    artist_dropdown = ttk.Combobox(ui_frame, textvariable=artist_filter)
    artist_dropdown['values'] = ["All Artists"] + artist_names
    artist_dropdown.grid(row=0, column=1, padx=5, pady=5)
    
    def update_song_list():
        artist = artist_filter.get()
        if artist == "All Artists":
            new_song_names = recommendations.songs['song'].tolist()
        else:
            new_song_names = recommendations.songs[recommendations.songs['artist'] == artist]['song'].tolist()
        
        dropdown['values'] = new_song_names
        selected_song.set('')


    def show_recommendations():
        song = selected_song.get()
        artist = artist_filter.get()
        number_songs = 10

        recom_song = recommendations.recommend(song, number_songs)
        
        if artist != "All Artists":
            recom_song = [item for item in recom_song if item[2] == artist]
        
        for widget in result_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(result_frame, text=f"Recommended songs for '{song}' by '{artist}':").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        for i, (score, song_name, artist_name) in enumerate(recom_song):
            ttk.Label(result_frame, text=f"{i+1}. {song_name} by {artist_name} (Score: {round(score, 3)})").grid(row=i+1, column=0, padx=5, pady=2, sticky="w")


    #---------------------------------------------------------------------------------#

    # def show_recommendations():
    #     song = selected_song.get()
    #     number_songs = 5
    #     recom_song = recommendations.recommend(song, number_songs)
    
    #     for widget in result_frame.winfo_children():
    #         widget.destroy()
    
    #     ttk.Label(result_frame, text=f"Recommended songs for '{song}':").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    #     for i, (score, song_name, artist) in enumerate(recom_song):
    #         ttk.Label(result_frame, text=f"{i+1}. {song_name} by {artist} (Score: {round(score, 3)})").grid(row=i+1, column=0, padx=5, pady=2, sticky="w")
    def filter_by_artist():
        artist = artist_filter.get()
        song = selected_song.get()
        number_songs = 10
        
        if artist == "All Artists":
            recom_song = recommendations.recommend(song, number_songs)
        else:
            recom_song = [item for item in recommendations.recommend(song, number_songs) if item[2] == artist]
        
        for widget in result_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(result_frame, text=f"Filtered recommendations for '{song}' by '{artist}':").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        for i, (score, song_name, artist_name) in enumerate(recom_song):
            ttk.Label(result_frame, text=f"{i+1}. {song_name} by {artist_name} (Score: {round(score, 3)})").grid(row=i+1, column=0, padx=5, pady=2, sticky="w")

    filter_button = ttk.Button(ui_frame, text="Filter by Artist", command=update_song_list)
    filter_button.grid(row=0, column=2, padx=5, pady=5)
    button = ttk.Button(ui_frame, text="Get Recommendations", command=show_recommendations)
    button.grid(row=1, column=2, padx=5, pady=5)
    # Create a frame for the recommendations
    global result_frame
    # Create a canvas for the result_frame with a scrollbar
    result_canvas = tk.Canvas(root, height=200)
    result_canvas.place(relx=0.5, rely=0.5, anchor=tk.N)  # Positioned below the ui_frame

    # Create a vertical scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_canvas.yview)
    scrollbar.place(relx=0.75, rely=0.5, height=200, anchor=tk.N)
    
    # Create a frame within the canvas for the recommendations
    result_frame = ttk.Frame(result_canvas, padding="10", style='TFrame')
    result_frame.bind("<Configure>", lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))
    
    result_canvas.create_window((0, 0), window=result_frame, anchor="nw")
    result_canvas.configure(yscrollcommand=scrollbar.set)
    
    root.mainloop()


# Create the welcome window
welcome_window = tk.Tk()
welcome_window.title("Welcome")
welcome_window.geometry("800x600")  # Fixed size for the welcome window

# Load the background image
background_image = Image.open("images/istockphoto-1076840920-612x612.jpg")
background_image = background_image.resize((800, 600), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(welcome_window, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create a transparent frame
welcome_frame = ttk.Frame(welcome_window, padding="20")
welcome_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create the welcome label with increased font size
welcome_label = ttk.Label(welcome_frame, text="Welcome to the Song Recommendation Model", font=("Helvetica", 18))
welcome_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# Create Enter and Exit buttons
enter_button = ttk.Button(welcome_frame, text="Enter", command=open_recommendation_system)
enter_button.grid(row=1, column=0, padx=5, pady=10)

exit_button = ttk.Button(welcome_frame, text="Exit", command=exit_application)
exit_button.grid(row=1, column=1, padx=5, pady=10)

welcome_window.mainloop()
