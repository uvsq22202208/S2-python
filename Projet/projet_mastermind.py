import tkinter as tk

8 couleurs:
bleu (1)
vert (2)
rouge (3)
violet (4)
jaune (5)
orange (6)
blanc (7)
noir (8)

dico_couleurs = {'bleu': 1 , 'vert': 2, 'rouge': 3, 'violet': 4 , 'jaune': 5 , 'orange': 6 , 'blanc': 7 , 'noir': 8}


4 pions composant le code 

10 essais

def placement_pion (l, l1):
    for i in range(len(l)):
        if l1[i] == l[i]:
            print ("bien placé")
        elif (l1[i] in l) and (l1[i] != l[i]):
            print ("mal placé")