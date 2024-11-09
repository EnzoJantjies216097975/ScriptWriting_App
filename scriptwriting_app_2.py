import tkinter as tk
from tkinter import ttk, messagebox

# Function for dropdown menu options
def show_option(option):
    messagebox.showinfo("Option Selected", f"You selected: {option}")

# Function to handle buttons (placeholders)
def button_action(name):
    messagebox.showinfo("Action", f"{name} button clicked!")

# Main window setup
root = tk.Tk()
root.title("New Story")
root.geometry("1000x600")

# Top Main Panel (with buttons and dropdown menu)
top_panel = tk.Frame(root, bg="lightgray")
top_panel.pack(side="top", fill="x", padx=5, pady=5)

# Back button and story title
back_button = tk.Button(top_panel, text="Back", command=lambda: button_action("Back"))
back_button.pack(side="left", padx=5)

title_label = tk.Label(top_panel, text="New Story Title", font=("Helvetica", 16))
title_label.pack(side="left", padx=5)

# Right side buttons
button_names = ["Home", "Timeline", "Cards", "Page", "Characters", "Story Stats", "View Slideshow"]
for name in button_names:
    btn = tk.Button(top_panel, text=name, command=lambda n=name: button_action(n))
    btn.pack(side="right", padx=2)

# Dropdown menu for options
menu_button = tk.Menubutton(top_panel, text="Options", relief="raised")
menu = tk.Menu(menu_button, tearoff=0)
options = ["Edit Details", "Find and Replace", "Sharing & Permissions", "Copy", "Scene Images", "Download As",
           "Print", "Advanced Options"]
for option in options:
    menu.add_command(label=option, command=lambda opt=option: show_option(opt))
menu_button.config(menu=menu)
menu_button.pack(side="right", padx=5)

# Main middle panel
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=5, pady=5)

# Left panel setup
left_panel = tk.Frame(main_frame, bg="lightblue", width=300)
left_panel.pack(side="left", fill="y", padx=5)

# Entry for genre and title
genre_entry = ttk.Entry(left_panel)
genre_entry.insert(0, "Genre")
genre_entry.pack(pady=5, fill="x")

title_entry = ttk.Entry(left_panel)
title_entry.insert(0, "Title of Story")
title_entry.pack(pady=5, fill="x")

# Navigation buttons in the left panel
nav_buttons = ["Timeline", "Cards", "Page", "Characters", "Story Stats", "Slides", "Share"]
for nav in nav_buttons:
    btn = tk.Button(left_panel, text=nav, command=lambda n=nav: button_action(n))
    btn.pack(pady=2, fill="x")

# Logline text box
logline_text = tk.Text(left_panel, height=3)
logline_text.insert("1.0", "Logline")
logline_text.pack(pady=5, fill="x")

# Add theme button
theme_button = tk.Button(left_panel, text="Add Theme", command=lambda: button_action("Add Theme"))
theme_button.pack(pady=5)

# Characters section
characters_label = tk.Label(left_panel, text="Characters", bg="lightblue")
characters_label.pack(pady=5)
add_character_button = tk.Button(left_panel, text="Add Character", command=lambda: button_action("Add Character"))
add_character_button.pack(pady=5, fill="x")

# Written by option (dropdown)
bio_option = ttk.Combobox(left_panel, values=["Show Bio", "Hide Bio"])
bio_option.set("Show Bio")
bio_option.pack(pady=5, fill="x")

# Credits text box
credits_text = tk.Text(left_panel, height=3)
credits_text.insert("1.0", "Credits")
credits_text.pack(pady=5, fill="x")

# Right panel setup
right_panel = tk.Frame(main_frame, bg="lightgreen")
right_panel.pack(side="right", expand=True, fill="both", padx=5)

scene_label = tk.Label(right_panel, text="Scene Slides", bg="lightgreen", font=("Helvetica", 14))
scene_label.pack(pady=5)

scene_info = tk.Label(right_panel, text="Scenes added to the slideshow will appear here.", bg="lightgreen")
scene_info.pack(pady=5)

timeline_button = tk.Button(right_panel, text="Go to Timeline", command=lambda: button_action("Go to Timeline"))
timeline_button.pack(pady=10)

# Start the main loop
root.mainloop()
