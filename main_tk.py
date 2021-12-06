"""
Created on Mon Dec  6 15:10:16 2021

@author: audrey.nicolle et emma.begard

to do : faire tourner le jeu sous tkinter
"""
#Import -----------------------------------------------------------------------
from tkinter import Tk,Label, Button, StringVar, Entry
import bibliotheque as b

def run_game () :
    """ 
    brief : on a pas fait 
    """    

    
#creation fenetre
ma_fenetre = Tk()
ma_fenetre.title('Jeu du Pendu')
#creation widget du mot lors de la partie
mot = Label(ma_fenetre, text = b.init_affichage(b.find_word('fichier_mots')))
mot.pack(side = 'top', padx = 5, pady = 5) 

#creation du widget du nombre de vie lors de la partie
nb_vie = Label(ma_fenetre, text = 'vie')
nb_vie.pack(side ='top',padx = 5, pady = 5)


# Creation bouton proposer 
bouton_proposer = Button(ma_fenetre, text = 'Proposer', command = run_game)
bouton_proposer.pack(side = 'left', padx = 5, pady = 5)

#creation du champ pour entrer sa lettre
lettre_propose = StringVar() 
champ = Entry(ma_fenetre,textvariable = lettre_propose)
champ.pack(side = 'right', padx = 5, pady = 5)

ma_fenetre.mainloop()
