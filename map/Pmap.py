from map import Player
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_pont_suspendu = [
        ["🌉", "🌉", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉"," ", " ",  " ", " ", " ", " ", " ", " ", " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"]
    ]


descriptions = {
    "🌉": "\033[33mVous êtes sur un pont suspendu, le vide est immense en dessous de vous.\033[0m",
}

position_joueur = [2, 2]

def afficher_carte():
    clear_screen()
    for i, ligne in enumerate(carte_pont_suspendu):
        ligne_affichee = ""
        for j, lieu in enumerate(ligne):
            if [i, j] == position_joueur:
                ligne_affichee += "⚔️  "
            else:
                ligne_affichee += lieu + " "
        print(ligne_affichee)
    print("\n")
    
    

def deplacer_joueur(commande):
    x, y = position_joueur
    nouvelle_position = [x, y]
    if commande == "z":
        nouvelle_position[0] -= 1
    elif commande == "s":
        nouvelle_position[0] += 1
    elif commande == "q":
        nouvelle_position[1] -= 1
    elif commande == "d":
        nouvelle_position[1] += 1

    if est_deplacement_valide(nouvelle_position):
        position_joueur[0], position_joueur[1] = nouvelle_position
    else:
        print("Déplacement impossible.")

def est_deplacement_valide(nouvelle_position):
    x, y = nouvelle_position
    return 0 <= x < len(carte_pont_suspendu) and 0 <= y < len(carte_pont_suspendu[0]) and carte_pont_suspendu[x][y] != "#"

def boucle_jeu(joueur):
    while True:
        afficher_carte()
        commande = input("Entrez une commande (z, q, s, d ou quitter) : ").lower()
        if commande == "quitter":
            print("Quitter le jeu...")
            break
        else:
            deplacer_joueur(commande)
