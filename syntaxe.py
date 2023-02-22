'''
Created on 28  Fev 2022
@author: menez

Syntax analysis of the file of frames 
'''

import binascii
#====================================================
def readtrames(filename):
    """
    Cette fonction fabrique une liste de chaines de caracteres a partir du 
    fichier contenant les trames.
    
    Chaque chaine de la liste rendue est une trame du fichier.
    
    return : liste des trames contenues dans le fichier
    """
    file = open(filename)
    lestrames = [] # List of frames (= lestrames)
    trame = ""  # Current frame .. string vide
    i = 1
    for line in file : # acces au fichier ligne par ligne
        line = line.rstrip('\n') # on enleve le retour chariot de la ligne
        line = line[4:53]        # on ne garde que les colonnes interessantes  
        print ("ligne {} : {}".format(i,line))
        trame = trame + line

        if (len(line) == 0): # Trame separator
            
            # On enregistre la trame dans lestrames
            trame = trame.replace(' ','') # on enleve les blancs
            lestrames.append(trame) # on ajoute la trame a la liste 
            trame = ""       # reset trame
        i = i+1
        
    # Si a la fin du fichier, il reste une trame à enregister 
    if len(trame) != 0 : # Last frame
        trame = trame.replace(' ','') # on enleve les blancs
        lestrames.append(trame) # on ajoute la trame a la liste 

    return lestrames

def unhexlify_lestrames(l):
    ''' l : liste de trames '''
    for i,trame in enumerate(l):
        print("{}({})".format(type(trame),len(trame)),end='')
        l[i] = binascii.unhexlify(trame) 
        print("   --> {}({}) : {} ...".format(type(trame), len(trame), trame[0:10]))

def analyse_syntaxique(filename) :
    ''' Analyse syntaxique du fichier filename'''

    # Transformation des echanges contenus dans le fichier
    # vers une liste de strings :  une string = une trame
    print("="*60)
    trames = readtrames(filename)

    print("="*60)
    print("\nTrames lues depuis le fichier :\n")
    for i,t in enumerate(trames):
        print("trame #{} : {}".format(i,t))

    # Unhexlify la liste de trames
    unhexlify_lestrames(trames)

    return trames

#=================================================================
if __name__ == '__main__':

    filename = "tramz.txt"
    #filename = "a_req.txt"
    #filename = "d_req.txt"
    #filename = "hbin_org.txt"
    #filename = "p_req.txt"
    #filename = "pnull_req.txt"
    #filename = "s_req.txt"

    # Analyse syntaxique
    analyse_syntaxique(filename)
