import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import mysql.connector
import io

# Connexion à la base de données MySQL à distance
def get_images_from_db():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host='localhost',          # Adresse de l'hôte (localhost dans ce cas)
            user='root',    # Ton utilisateur MySQL
            password='root', # Ton mot de passe MySQL
            database='employees'   # Nom de ta base de données
        )
        
        cursor = conn.cursor()

        # Requête SQL pour récupérer les images (imaginons une table `user_images`)
        cursor.execute('SELECT image_name, image_data FROM user_images')
        
        # Récupérer toutes les lignes
        images = cursor.fetchall()
        
        # Fermeture de la connexion
        conn.close()
        return images

    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")
        return []

# Crée la fenêtre principale
root = tk.Tk()
root.title("Affichage des photos des utilisateurs")

# Liste des images récupérées depuis la base de données
images = get_images_from_db()

# Vérification si des images ont été récupérées
if not images:
    print("Aucune image trouvée dans la base de données.")
    root.quit()  # Quitte l'application si aucune image n'est trouvée

# Variable d'index pour gérer l'image courante
current_index = 0

# Fonction pour afficher l'image suivante
def next_image():
    global current_index
    current_index = (current_index + 1) % len(images)
    display_image()

# Fonction pour afficher l'image précédente
def prev_image():
    global current_index
    current_index = (current_index - 1) % len(images)
    display_image()

# Fonction pour afficher l'image courante
def display_image():
    image_name, image_data = images[current_index]
    img = Image.open(io.BytesIO(image_data))  # Convertir le BLOB en image
    img = img.resize((300, 300))  # Redimensionner l'image
    img = ImageTk.PhotoImage(img)

    label.config(image=img)
    label.image = img  # Garder une référence de l'image
    label_text.config(text=image_name)

# Crée une étiquette pour afficher l'image
label = tk.Label(root)
label.pack()

# Crée une étiquette pour afficher le nom de l'image
label_text = tk.Label(root, text="", font=("Arial", 14))
label_text.pack()

# Crée des boutons pour naviguer
prev_button = tk.Button(root, text="Précédent", command=prev_image)
prev_button.pack(side=tk.LEFT)

next_button = tk.Button(root, text="Suivant", command=next_image)
next_button.pack(side=tk.RIGHT)

# Affiche la première image
display_image()

# Lance l'interface graphique
root.mainloop()
