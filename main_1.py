#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:56:58 2021

@author: emma.begard
"""

import bibliotheque as b




def main(file):
    """
     fait touner le jeux tant que l'on veut continuer à jouer
         
         file :  le fichier contenant tt les mots 
    """
    play =True
    score = 0
    
    while play :
        
        # we once
        score += b.partie(True, file)
        print('Vous avez un score de :{}'.format(score) )
        
        # if we wanna play again
        reponse = b.play_again()
        
        if reponse== False:
            print('Vous avez un score de :{}'.format(score) )
            play = False


main("fichier_mots.txt")