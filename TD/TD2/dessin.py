import tkinter as tk
import random


def disque():
    a = random.randint (0, 600)
    b = random.randint (0, 600)
    c = random.randint (0, 600)
    d = random.randint (0, 600)
    canvas.create_oval (a, b, c, d,fill="purple")


racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre
canvas = tk.Canvas(racine, bg="black", height=600, width=600, highlightthickness=20, relief = "raised")
cercle = tk.Button(racine, text="cercle", font = ("helvetica", "13"), command = disque)
carre = tk.Button(racine, text="carré", font = ("helvetica", "13"))
croix = tk.Button(racine, text="croix", font = ("helvetica", "13"))
choix_couleur = tk.Button(racine, text="choisir une couleur", font = ("helvetica", "13"))
choix_couleur.grid(column=1, row = 0)
cercle.grid (column = 0, row = 1)
carre.grid (column = 0, row = 2)
croix.grid (column = 0, row = 3)
canvas.grid(row = 1, column = 1, rowspan = 3)
racine.mainloop() # Lancement de la boucle principale







    