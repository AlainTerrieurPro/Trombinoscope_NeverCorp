import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

# Crée la fenêtre principale
root = tk.Tk()
root.title("Affichage des photos des utilisateurs")

# Chemin du dossier photos
photos_dir = 'photos'

# Liste des fichiers image dans le dossier
photos = [f for f in os.listdir(photos_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Variable d'index pour gérer l'image courante
current_index = 0

# Fonction pour afficher l'image suivante
def next_image():
    global current_index
    current_index = (current_index + 1) % len(photos)
    display_image()

# Fonction pour afficher l'image précédente
def prev_image():
    global current_index
    current_index = (current_index - 1) % len(photos)
    display_image()

# Fonction pour afficher l'image courante
def display_image():
    img_path = os.path.join(photos_dir, photos[current_index])
    img = Image.open(img_path)
    img = img.resize((300, 300))  # Redimensionner l'image pour l'afficher
    img = ImageTk.PhotoImage(img)

    label.config(image=img)
    label.image = img  # Garder une référence de l'image

# Crée une étiquette pour afficher l'image
label = tk.Label(root)
label.pack()

# Crée des boutons pour naviguer
prev_button = tk.Button(root, text="Précédent", command=prev_image)
prev_button.pack(side=tk.LEFT)

next_button = tk.Button(root, text="Suivant", command=next_image)
next_button.pack(side=tk.RIGHT)

# Affiche la première image
display_image()

# Lance l'interface graphique
root.mainloop()
