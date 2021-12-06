#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:28:47 2021

@author: emma.begard

 to do:
     
     fonction qui recupère un mot au hazard dans un fichier
     fonction qui verifit si la saisie est dans le mot
     fonction qui affiche la lettre une fois qu'elle a été trouvée, et celles d'avant aussi
     
     
     
"""
import random as rd

def find_word(file):
    """
        find a word within the file and returns a liste composed of the word's letters
   
        Parameters
        ----------
        file : str
            the file's followed of its extension (ex : tste.txt).
    
        Returns
        -------
        lst[]

    """
    # the list with all the words within the file
    lst = []
    # the word divided by letters
    word= []
    with open(file, 'r') as doc:
        
        lignes = doc.readlines()
        for ligne in lignes :
            
            # we get all the words of the line
            a = ligne.split(" ")
            # we remove the _\n at the end of the line
            a[len(a)-1 ] = a[len(a)-1 ][:-1]
            # we add all the word to our list of words
            lst.extend(a)
    
    # a word within the list of words
    num = rd.randint( 0, len(lst) )
    # making a list out of the word's letters
    for lettre in lst[num]:
        word.append(lettre)
    return word
    
def vie (vie, return_recherche ):
    """
    updates the life bar 
    
    Parameters
    ----------
    vie : int
        the life before the letter is recherched.
    return_recherche : teh result of the function recherche
        a tuple ( True/False, indice/-1)

    Returns
    -------
    vie : int
        the life left.

    """
    
    if return_recherche == False :
        vie -= 1
        
    return vie
    
def recherche(lst_lettre_mot, lettre) :
     """ 
     breif : recherche la lettre donné par le joueur dans le mot. Si la lettre
             est dans le mot, on donne sa position dans le mot et la valeur true
             ou alors on retourne False et -1.
     param : lst_lettre_mot => liste qui contient les lettres du mots.(lst)
             lettre => lettre donné par le joueur (input programme principal)(str)
     retval : tuple(Booléen,position de la lettre dans le mot ou -1).
     """
     #on recherche la lettre dans le mot 
     for indice,L in enumerate(lst_lettre_mot) : 
         if L == lettre : 
             return (True,indice)
         return (False,-1)
         
    
def affichage (affiche,lst_lettre_mot,lettre, valeur_vie) :
     """
     breif : affiche les lettres du mot ou des underscores si la lettre n'a pas 
             été deviné
     param : lst_lettre_mot => liste qui contient les lettres du mots.(lst)
             T_pos_lettre => (booleen,poqition de la lettre dans le mot (int))(tuple)
     retval : affiche => str du mot que le joueur voit ou la str "ok" si le joeur 
             a gagné
     """
     if lettre.lower() in ['1','2','3','4','5','6','7','8','9']:
         return "Vous n'avez pas rentré une lettre"
     
     vie_restante = vie(valeur_vie,recherche)
     T_pos_lettre = recherche(lst_lettre_mot,lettre)
     
     if T_pos_lettre[0] :
         affiche[T_pos_lettre[1]] = lettre
         print(affiche,"/n Nombre de chance restante : " + vie_restante)
         if not '_' in affiche : # on verifie si le joueur a trouvé le mot en entier
             print("Bravo ! C'est gagné !")
             return "ok"            
     else : 
         print("Attention, la pendaison se rapproche. /n \
               Nombre de chance restante : "  + vie_restante)
    
     return affiche      