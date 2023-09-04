import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to move files
def move_images(source_folder, dest_folder):
    for filename in os.listdir(source_folder):
        if filename.startswith("IMG_"):
            base_name = filename[4:]
            matching_file = "IMG_E" + base_name
            if matching_file in os.listdir(source_folder):
                source_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(dest_folder, filename)
                shutil.move(source_path, dest_path)

# Function to handle the button click event
def process_folder():
    selected_folder = filedialog.askdirectory(title="Select a folder")
    if selected_folder:
        new_folder = os.path.join(selected_folder, "folder_IMG_")
        os.makedirs(new_folder, exist_ok=True)
        move_images(selected_folder, new_folder)
        print("Images moved successfully!")

# Create a GUI window
root = tk.Tk()
root.title("Image Mover")

# Create a button to select a folder
select_folder_button = tk.Button(root, text="Select Folder", command=process_folder)
select_folder_button.pack(padx=20, pady=20)

# Run the GUI application
root.mainloop()
