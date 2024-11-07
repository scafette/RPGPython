
from player import Player
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," ","H"," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," ","P"," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "M", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," ","J"," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]



descriptions = {
    "F": "\033[33mLa Fosse des Ombres:\033[0m Une vaste cavité souterraine au sein du sanctuaire, enveloppée dans une brume obscure.\n"
         "Les murs sont recouverts de racines et de mousse, et l'air est épais de magie ancienne.",
    "P": "\033[33mLe Pont Suspendu:\033[0m Un pont étroit et branlant suspendu au-dessus d’un abîme sans fond.\n"
         "Le vent souffle si fort que chaque pas semble incertain. De mystérieuses silhouettes volantes se déplacent au loin.",
    "J": "\033[33mLe Jardin des Ruines:\033[0m Un ancien jardin oublié, envahi par la végétation et les ruines de statues brisées.\n"
         "Les plantes ici sont étranges, certaines semblent presque vivantes.",
    "C": "\033[33mLa Chambre du Cristal:\033[0m Une salle secrète au cœur du sanctuaire, où un gigantesque cristal lumineux flotte en lévitation.\n"
         "Des éclats de lumière magique jaillissent à intervalles réguliers, rendant l'atmosphère à la fois mystique et inquiétante.",
    "M": "\033[33mLe Hall des Murmures:\033[0m Un long couloir rempli d'échos incessants.\n"
         "Des runes luminescentes flottent sur les murs, chuchotant des paroles incompréhensibles. "
         "La lumière est faible, rendant l’atmosphère oppressante.",
    "T": "\033[33mLa Cour des Titans:\033[0m Une immense cour ouverte entourée de statues géantes de guerriers antiques.\n"
         "Certaines statues semblent presque respirer, comme si elles pouvaient s’animer à tout moment.",
    "H": "\033[33mLa Tour des Hurlements:\033[0m La tour principale du sanctuaire, où les vents soufflent si fort qu’ils semblent hurler.\n"
         "Les escaliers sont en ruine, et chaque étage abrite de nouveaux dangers."
}


position_joueur = [0, 0]

def afficher_carte():
    clear_screen()
    for i, ligne in enumerate(carte):
        ligne_affichee = ""
        for j, lieu in enumerate(ligne):
            if [i, j] == position_joueur:
                ligne_affichee += "♱ "
            else:
                ligne_affichee += lieu + " "
        print(ligne_affichee)
    print("\n")

def deplacer_joueur(commande):
    x, y = position_joueur
    if commande == "z" and x > 0:  # Haut
        position_joueur[0] -= 1
    elif commande == "s" and x < len(carte) - 1:  # Bas
        position_joueur[0] += 1
    elif commande == "q" and y > 0:  # Gauche
        position_joueur[1] -= 1
    elif commande == "d" and y < len(carte[0]) - 1:  # Droite
        position_joueur[1] += 1
    else:
        print("Déplacement impossible.")
        
        

def est_deplacement_valide(nouvelle_position):
    x, y = nouvelle_position
    if 0 <= x < len(carte) and 0 <= y < len(carte[0]) and carte[x][y] != "#":
        return True
    clear_screen()
    return False


def description_lieu():
    x, y = position_joueur
    lieu = carte[x][y]
    description = descriptions.get(lieu, "un endroit inconnu")
    print(f"Vous êtes dans : {description}\n")
    while True:
        if lieu == "F":
            print("Souhaitez vous explorer la Fosse des Ombres ou Fuir ?")
            choix = input("Entrez votre choix (explorer, fuir) : ").lower()
            if choix == "explorer":
                print("Vous explorez la Fosse des Ombres...")
                break
            
    



def boucle_jeu(joueur):
    while True:
        afficher_carte()
        description_lieu()
        
        commande = input("Entrez une commande (z, q, s, d ou Quitter) : ").lower()
        if commande == "quitter":
            print("Quitter le jeu...")
            break
        else:
            deplacer_joueur(commande)
