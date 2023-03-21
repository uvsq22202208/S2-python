import tkinter as tk

v1 = int(input("Choisir la première valeur"))
v2 = int(input("Choisir la deuxième valeur"))
def demander_nombre ():
    int(input("Choisir une valeur"))

racine = tk.Tk()
labela = tk.Button(racine, text = "Choisir une valeur pour l'opérande gauche", font = ("helvetica", "26"))
labelb = tk.Button(racine, text = "Choisir une valeur pour l'opérande droite", font = ("helvetica", "26"))
labelc = tk.Label(racine, text = "?", font = ("helvetica", "26"))
labeld = tk.Label(racine, text = "+", font = ("helvetica", "26"))
labele = tk.Label(racine, text = "?", font = ("helvetica", "26"))
labelf = tk.Label(racine, text = "=", font = ("helvetica", "26"))
labelg = tk.Label(racine, text = "?", font = ("helvetica", "26"))
labelh = tk.Button(racine, text = "calculer", font = ("helvetica", "26"))
labela.grid(column=0, row=1)
labelb.grid(column=0, row=2)
labelc.grid(column=2, row=0)
labeld.grid(column=3, row=0)
labele.grid(column=4, row=0)
labelf.grid(column=5, row=0)
labelg.grid(column=6, row=0)
labelh.grid(column=4, row=1)
racine.mainloop()










import tkinter as tk

def affichage(texte):
    """ Modifie le texte d'un label. """
    label.config(text=texte)

racine = tk.Tk() # Création de la fenêtre racine
label = tk.Label(racine, text="", padx=20, pady=20, font = ("helvetica", "30"))
label.grid(row=0, column=0, columnspan=2)
bouton1 = tk.Button(racine, text="affichage 1", command=lambda : affichage("ils sont fous ces romains"),
                     font = ("helvetica", "30")
                   ) 
bouton1.grid(row=1, column=0) 
bouton2 = tk.Button(racine, text="affichage 2", 
                    command=lambda : affichage("quand lama faché, lui toujours faire ainsi"),
                    font = ("helvetica", "30") 
                   )
bouton2.grid(row=1, column=1) 
racine.mainloop() # Lancement de la boucle principale

import tkinter as tk


racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=100, width=100)
canvas.grid()
racine.mainloop() # Lancement de la boucle principale5
