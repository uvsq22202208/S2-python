import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre
canvas = tk.Canvas(racine, bg="black", height=600, width=600)
cercle = tk.Button(racine, text="cercle", font = ("helvetica", "13"))
carre = tk.Button(racine, text="carré", font = ("helvetica", "13"))
croix = tk.Button(racine, text="croix", font = ("helvetica", "13"))
choix_couleur = tk.Button(racine, text="choisir une couleur", font = ("helvetica", "13"))
choix_couleur.grid(column=1, row = 0)
cercle.grid (column = 0, row = 1)
carre.grid (column = 0, row = 2)
croix.grid (column = 0, row = 3)
canvas.grid(row = 1, column = 1, rowspan = 3)
racine.mainloop() # Lancement de la boucle principale

