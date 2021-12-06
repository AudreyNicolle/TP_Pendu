#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:28:47 2021

@author: emma.begard et audrey.nicolle

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
    num = rd.randint( 0, len(lst)-1 )
    # making a list out of the word's letters
    for lettre in lst[num]:
        word.append(lettre)
        
    print("le mot a trouver est ", word)
    return word
    
def fonc_vie (vie, return_recherche ):
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

    ind = []
    is_here = False
    
    #we look for the letter in teh word
    for indice,L in enumerate(lst_lettre_mot) : 
        
        if L == lettre : 
            ind.append(indice)
    # if we found 'letter' once or more        
    if len(ind) != 0:
        return(True, ind)
    
    else :
        return(False, [])


def affichage (affiche,lst_lettre_mot, lettre) :
    """
     breif : affiche les lettres du mot ou des underscores si la lettre n'a pas 
             été deviné
     param : lst_lettre_mot => liste qui contient les lettres du mots.(lst)
             T_pos_lettre => (booleen,poqition de la lettre dans le mot (int))(tuple)
             lettre => the letter
     retval : affiche => str du mot que le joueur voit 
             end => True si le jouer a trouvé, sinon False
     """
    

    # a tuple ( True: the letter is in teh word, indice)
    T_pos_lettre = recherche(lst_lettre_mot,lettre)
    
    print("mot dans affiche avant remplacement", affiche)

    # if the letter is in the word
    if T_pos_lettre[0] :
        
        end = False
       
        for i in T_pos_lettre[1]:
            # we remove the '_'
            affiche = affiche[0:i]+str(lettre)+affiche[i+1:]
            # the str of teh word and if we found the word
            
        if not '_' in affiche : # on verifie si le joueur a trouvé le mot en entier
            end = True
               
        return (affiche, end)

    return (affiche, False)
 
def init_affichage(lst_lettre_mot):
    """ 
    brief : initialise l'affichage du mot pour le joueur'
    param : lst_lettre_mot => liste qui contient les lettres du mots.(lst)
    retval : l'affichage du mot ou on voit la première lettre et des underscores
    """
    underscore =''
    i = 0
    while i < len(lst_lettre_mot)-1 : 
        underscore += '_'
        i = i+1
    return lst_lettre_mot[0] + underscore

def saisie() :
    """"
    breif : permet de récupérer le mot saisi par l'utilisateur
    param : none
    retval : rappel saisie si lettre non conforme ou retourne la lettre
    """
    lettre = input("Veuillez saisir une lettre : ")
    if lettre.lower() in ['1','2','3','4','5','6','7','8','9']:
        print( "Vous n'avez pas rentré une lettre")
        return saisie()
    else :
        return lettre 
    
    
def play_again():
    """
    allow us to play as much as we want
    """
    val = input('Voulez-vous rejouer ? : Oui:O Non:N \n')
    if val =="O":
        return True
    elif val =="N":
        return False
    else :
        print("Erreur de saisie")
        return play_again()


def partie(run, file):
    """ 
    The main programme 
    run : a boolean to run the game
    file : the file with all the words
    """
    vie = 8
    # we choose a word
    word = find_word(file)
    # initialisation of the "_" list
    affiche = init_affichage(word)
    print("Le mot à deviner est " ,affiche)

    while run :
        
        #initailisation des differentes variables
        lettre = saisie()
        
        #print("dans while", affiche)
        if vie > 0:
            
            result= affichage(affiche, word, lettre)
            affiche = result[0]
            fin =result[1]
            vie = fonc_vie(vie, recherche(word,lettre)[0])
            print("Le mot à deviner est ", affiche)
            print("points de vie", vie)
            
            if fin :
                print("Gagné !")
                return +1

        else :
            print("Perdu !")
            run = False
            return -1
    """"
    breif : permet de récupérer le mot saisi par l'utilisateur
    param : none
    retval : rappel saisie si lettre non conforme ou retourne la lettre
    """
    lettre = input("Veuillez saisir une lettre : ")
    if lettre.lower() in ['1','2','3','4','5','6','7','8','9']:
        print( "Vous n'avez pas rentré une lettre")
        return saisie()
    else :
        return lettre  
