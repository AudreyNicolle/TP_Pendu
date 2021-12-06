#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:28:47 2021

@author: emma.begard
   
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
    
def main(run= True, file):
    """ 
    The main programme 
    """

    word = find_word(file)

    while run :

        affichage()
