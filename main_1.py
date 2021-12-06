import bibliotheque as b

def main(run= True, file):
    """ 
    The main programme 
    """
    vie = 8
    word = b.find_word(file)
    # initialisation of the "_" list
    affiche = b.init_affichage(word)

    while run :

        if vie >= 1:

            if b.affichage(affiche, word, vie)== 'ok':
                vie = 0
            else :
                vie = b.vie(vie)
                affiche = b.affichage(affiche, word, vie)

        else :
            print("sorry, you lose")
            run = False