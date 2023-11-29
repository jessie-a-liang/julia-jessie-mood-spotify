import tkinter as tk
from tkinter import messagebox
import subprocess

def generate_playlist():
    try:
        subprocess.run(['python', 'Spotify.py'], check=True)
        messagebox.showinfo("Success", "Playlist generated successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Playlist Generator")

# Create a button that calls the generate_playlist function when clicked
generate_button = tk.Button(root, text="Generate Playlist", command=generate_playlist)
generate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()