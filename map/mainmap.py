import os
from map.Fmap import carte_fosse_ombres, descriptionsF
from map.Jmap import carte_jardin, descriptionsJ
from map.Pmap import carte_pont_suspendu, descriptionsP
from map.Tmap import carte_titan, descriptionsT
from map.Hmap import carte_hurlements, descriptionsH
from assets.items import items
from assets.combat import fight
from assets.player import Mephisto,Tharagon,Silvarak,Sang_Igris, Player
from assets.inv import Inventaire
from assets.asccii import ascii_art_2_lines,print_ascii
from assets.asccii import print_ascii, ascii_art_9_lines
from assets.asccii import ascii_art_7_lines, print_ascii
from assets.asccii import print_ascii, ascii_art_11
from assets.asccii import print_ascii, ascii_art_8_lines
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


carte = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "H", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "P", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "J", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

descriptions = {
    "F": "\033[35mVous apercevez un panneau où il est écrit : 'La Fosse des Ombres'.\033[0m",
    "P": "\033[36mUn écriteau gravé dans le bois indique : 'Le Pont Suspendu'.\033[0m",
    "J": "\033[32mUn panneau de pierre recouvert de mousse signale : 'Le Jardin des Ruines'.\033[0m",  
    "T": "\033[33mVous trouvez une plaque dorée portant l'inscription : 'La Cour des Titans'.\033[0m",
    "H": "\033[31mUne ancienne stèle indique : 'La Tour des Hurlements'.\033[0m",
}

spawn_position = [2, 2]
position_joueur = [2, 2]

def afficher_carte(map):
    clear_screen()
    for i, ligne in enumerate(map):
        ligne_affichee = ""
        for j, lieu in enumerate(ligne):
            if [i, j] == position_joueur:
                ligne_affichee += "⚔️ "
            else:
                ligne_affichee += lieu + " "
        print(ligne_affichee)
    print("\n")

def deplacer_joueur(commande, map):
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

    if est_deplacement_valide(nouvelle_position, map):
        position_joueur[0], position_joueur[1] = nouvelle_position
    else:
        print("Déplacement impossible.")

def est_deplacement_valide(nouvelle_position, map):
    x, y = nouvelle_position
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] != "#" and map[x][y] != "🌿" and map[x][y] !="💥" and map[x][y] != "🌑" and map[x][y] !="🌉" and map[x][y] !="🧱"

def description_lieu(map):
    global carte_actuelle, position_joueur
    x, y =  position_joueur
    lieu = map[x][y]
    if map == carte_fosse_ombres :
        description = descriptionsF
    elif map == carte_pont_suspendu :
        description = descriptionsP
    elif map == carte_jardin :
        description = descriptionsJ
    elif map == carte_titan :
        description = descriptionsT
    elif map == carte_hurlements :
        description = descriptionsH
    else :
        description = descriptions
        
    if lieu in description:
        print(description[lieu])
        if description == descriptions :
            explorer = input("Voulez-vous explorer ce lieu ? (oui/non) : ").lower()
            if explorer == "oui":
                print(f"Vous explorez {[lieu]}")
                input()
                if lieu == "F":
                    carte_actuelle = carte_fosse_ombres
                    position_joueur = spawn_position
                    
                    afficher_carte(carte_fosse_ombres)
                elif lieu == "P":
                    carte_actuelle = carte_pont_suspendu
                    position_joueur  = [1, 7]
                    afficher_carte(carte_pont_suspendu)
                elif lieu == "J":
                    carte_actuelle = carte_jardin
                    position_joueur = [3, 8]
                    afficher_carte(carte_jardin)
                elif lieu == "T":
                    carte_actuelle = carte_titan
                    position_joueur = [4, 4]
                    afficher_carte(carte_titan)
                elif lieu == "H":
                    carte_actuelle = carte_hurlements
                    position_joueur = [1, 1]
                    afficher_carte(carte_hurlements)


            else :
                print("Vous rebroussez chemin.")
        elif lieu =="☠️🪓" :
            print(print_ascii(ascii_art_2_lines))
            print("Mephisto le Faucher D'Ether vous attaque !")
            fight(Mephisto,joueur)
            carte_actuelle[13][18] = " "
            carte_actuelle[5][21] = "🔑"
        elif lieu == "🔑":
                print("\033[32mutilisez la clé pour ???????????\033[0m")
                input("\033[35mAppuyez sur une touche pour utiliser la clé\033[0m")
                print("\033[31mLa Fosse est entrain de s'effondrez sortez vite !!!!!\033[0m")
                time.sleep(3)
                if lieu == "🔑":
                    carte_actuelle = carte
                    position_joueur = spawn_position
                    afficher_carte(carte_actuelle)
                    carte_actuelle[2][5] = " "
                print("\033[32mVous avez réussi à sortir de la Fosse des Ombres vous revoila dans le sanctuaire.\033[0m")
        elif lieu == "🗡️" :
            add = input("\033[31mVoulez-vous ajouter cette épée à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Épée")
                carte_actuelle[2][17] = " "
            else:
                print("Vous continuez votre chemin.")

        elif lieu == "🌹" :
            add = input("\033[31mVoulez-vous ajouter cette fleur à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Ronce")
                joueur.inventory.getitem("Épée").add_enchant(joueur.inventory.getitem("Ronce"))
                carte_actuelle[10][10] = " "
            else:
                print("Vous continuez votre chemin.")
        elif lieu =="🧪":
            add = input("\033[31mVoulez-vous ajouter cette potion à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Potion")
                print(print_ascii((ascii_art_11)))
                carte_actuelle[6][15] = " "
        elif lieu == "⚗️":
            add = input("\033[31mVoulez-vous ajouter cette potion à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Potion")
                print(print_ascii((ascii_art_11)))
                carte_actuelle[2][21] = " "
            else:
                print("Vous continuez votre chemin.")
        elif lieu == "🧉":
            add = input("\033[31mVoulez-vous ajouter cette potion à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Potion")
                print(print_ascii((ascii_art_11)))
                carte_actuelle[6][20] = " "
            else:
                print("Vous continuez votre chemin.")
        elif lieu == "💊":
            add = input("\033[31mVoulez-vous ajouter cette potion à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Potion")
                print(print_ascii((ascii_art_11)))
                carte_actuelle[8][9] = " "
            else:
                print("Vous continuez votre chemin.")
        elif lieu == "🚪":
            print("Vous avez trouvé une porte.")
            ouvrir = input("Voulez-vous ouvrir la porte ? (oui/non) : ").lower()
            if ouvrir == "oui":
                print("Vous ouvrez la porte...")
                input("Appuyez sur une touche pour continuer...")
                carte_actuelle = carte
                position_joueur = spawn_position
                afficher_carte(carte_actuelle)
                carte_actuelle[10][18] = " "
        elif lieu == "🔱👹":
            print("\033[31mTharagon le Roi des Titans vous attaque !\033[0m")
            print(print_ascii(ascii_art_8_lines))
            fight(Tharagon,joueur)
            carte_actuelle[6][13] = " "
            carte_actuelle[9][13] = "🔒"
        elif lieu == "🔒":
                print("\033[32mutilisez la clé pour ???????????\033[0m")
                input("\033[35mAppuyez sur une touche pour utiliser la clé\033[0m")
                print("\033[31mLa Cour des Titan est entrain de s'effondrez sortez vite !!!!!\033[0m")
                time.sleep(3)
                if lieu == "🔒":
                    carte_actuelle = carte
                    position_joueur = spawn_position
                    afficher_carte(carte_actuelle)
                    carte_actuelle[12][2] = " "
                print("\033[32mVous avez réussi à sortir de la Cours des Titans vous revoila dans le sanctuaire.\033[0m")
        elif lieu == "🐉":
            print(print_ascii(ascii_art_9_lines))
            print("\033[31mSilvarak le Dragon vous attaque !\033[0m")
            fight(Silvarak,joueur)
            carte_actuelle[10][13] = " "
            carte_actuelle[10][16] = "🗝️"
        elif lieu == "🗝️":
                print("\033[32mutilisez la clé pour ???????????\033[0m")
                input("\033[35mAppuyez sur une touche pour utiliser la clé\033[0m")
                print("\033[31mSilvarak crache ses flammes partout sur le pont sortez vite avant de mourir brulé !!!!!\033[0m")
                time.sleep(3)
                if lieu == "🗝️":
                    carte_actuelle = carte
                    position_joueur = spawn_position
                    afficher_carte(carte_actuelle)
                    carte_actuelle[5][22] = " "
                print("\033[32mVous avez réussi à sortir du Pont vous revoila dans le sanctuaire.\033[0m")
        elif lieu == "🤴🏻":
                print(print_ascii(ascii_art_7_lines))
                print("\033[31mSang Igris vous attaque !\033[0m")
                fight(Sang_Igris,joueur)
                print("\033[31mVous avez vaincu Sang Igris !\033[0m")
                print("\033[31mVous avez libéré l'âme de Caïd !\033[0m")
                print("\033[31mVous avez gagné !\033[0m")
                print("\033[31mMerci d'avoir joué !\033[0m")
                exit()

def boucle_jeu(name):
    global carte_actuelle, joueur
    carte_actuelle = carte
    joueur = Player(
        name=name,
        inventaire=Inventaire()
    )

    while True:
        afficher_carte(carte_actuelle)
        description_lieu(carte_actuelle)
        commande = input("Entrez une commande (z, q, s, d ou quitter) : ").lower()
        if commande == "quitter":
            print("Quitter le jeu...")
            break
        else:
            deplacer_joueur(commande,carte_actuelle)


# def searchItems(item):
#     for item in items:
#         return item