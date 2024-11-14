import os
from map.Cmap import carte_cristal, descriptionsC
from map.Fmap import carte_fosse_ombres, descriptionsF
from map.Mmap import carte_murmure, descriptionsM
from map.Jmap import carte_jardin, descriptionsJ
from map.Pmap import carte_pont_suspendu, descriptionsP
from map.Tmap import carte_titan, descriptionsT
# from assets.items import items
from assets.combat import fight
from assets.player import Mephisto,Tharagon,Player
from assets.inv import Inventaire
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
    ["#", " ", " ", " ", " ", " ", " ", " ", "M", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "J", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

descriptions = {
    "F": "\033[35mVous apercevez un panneau où il est écrit : 'La Fosse des Ombres'.\033[0m",
    "P": "\033[36mUn écriteau gravé dans le bois indique : 'Le Pont Suspendu'.\033[0m",
    "J": "\033[32mUn panneau de pierre recouvert de mousse signale : 'Le Jardin des Ruines'.\033[0m",  
    "C": "\033[34mUn symbole lumineux est gravé dans la pierre, indiquant : 'La Chambre du Cristal'.\033[0m", 
    "T": "\033[33mVous trouvez une plaque dorée portant l'inscription : 'La Cour des Titans'.\033[0m",
    "H": "\033[31mUne ancienne stèle indique : 'La Tour des Hurlements'.\033[0m",
    "M": "\033[31mUne ancienne stèle indique : 'Haul des Murmures'.\033[0m"
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
    return 0 <= x < len(carte) and 0 <= y < len(carte[0]) and carte[x][y] 
# != "#" and carte_jardin[x][y] != "🌿" and carte_titan[x][y] !="💥"


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
    elif map == carte_cristal :
        description = descriptionsC
    elif map == carte_titan :
        description = descriptionsT
    elif map == carte_murmure :
        description = descriptionsM
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
                    position_joueur = spawn_position
                    afficher_carte(carte_pont_suspendu)
                elif lieu == "J":
                    carte_actuelle = carte_jardin
                    position_joueur = spawn_position
                    afficher_carte(carte_jardin)
                elif lieu == "C":
                    carte_actuelle = carte_cristal
                    position_joueur = spawn_position
                    afficher_carte(carte_cristal)
                elif lieu == "T":
                    carte_actuelle = carte_titan
                    position_joueur = spawn_position
                    afficher_carte(carte_titan)
                elif lieu == "M":
                    carte_actuelle = carte_murmure
                    position_joueur = spawn_position
                    afficher_carte(carte_murmure)
                elif lieu == "M" :
                    carte_actuelle = carte_murmure
                    position_joueur = spawn_position
                    afficher_carte(carte_actuelle)

            else :
                print("Vous rebroussez chemin.")
        elif lieu =="☠️🪓" :
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
        elif lieu == "🌹" :
            add = input("\033[31mVoulez-vous ajouter cette fleur à votre inventaire ? (oui/non) : \033[0m").lower()
            if add == "oui":
                joueur.inventory.add("Ronce")
                joueur.inventory.add("Épée")
                joueur.inventory.getitem("Épée").add_enchant(joueur.inventory.getitem("Ronce"))
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
            fight(Tharagon,joueur)
            carte_actuelle[13][18] = " "
            carte_actuelle[5][21] = "🔑"
        elif lieu == "🔑":
                print("\033[32mutilisez la clé pour ???????????\033[0m")
                print("\033[34mutilisez la clé pour ???????????\033[0m")
                input("\033[35mAppuyez sur une touche pour utiliser la clé\033[0m")
                print("\033[31mLa Cour des Titan est entrain de s'effondrez sortez vite !!!!!\033[0m")
                time.sleep(3)
                if lieu == "🔑":
                    carte_actuelle = carte
                    position_joueur = spawn_position
                    afficher_carte(carte_actuelle)
                    carte_actuelle[12][2] = " "
                print("\033[32mVous avez réussi à sortir de la Cours des Titans vous revoila dans le sanctuaire.\033[0m")
                
                
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
            deplacer_joueur(commande)


# def searchItems(item):
#     for item in items:
#         return item