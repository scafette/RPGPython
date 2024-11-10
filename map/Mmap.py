from map import Player
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_murmure = [
        ["🚪", "🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "🌀", " ", " ", " ", " ", " ", " ", " ", " ", "💨", "💨", " "," ", "🌀", "🚪", "🚪"],
        ["🚪", "💨", "👁️‍🗨️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "👁️‍🗨️", "💨", "🌫️", "🌀", "💨", "🚪", "🚪"],
        ["🚪", "💨", "🌀", "💨", "💨", " ", " ", " ", " ", " ", " ", " ", "🌀", "💨", "💨", "🚪", "🚪"],
        ["🚪", "🌀", "🌫️", "👁️‍🗨️", "👁️‍🗨️", " ", " ", " ", " ", " ", " ", " ", "🌫️", "🌀", "🌫️", "🚪", "🚪"],
        ["🚪", "🌫️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "💨", "🚪"],
        ["🚪", "💨", "🌀", " ", " ", "🌀", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🚪", "🚪"],
        ["🚪", "💨", "👁️‍🗨️", "🌀", "🌀", "👁️‍🗨️", "💨", "🌀", "🚪", " ", " ", " ", " ", " ", " ", " ", "🚪"],
        ["🚪", "💨", "💨", " ", " ", "💨", " ", " ", "🚪", " ", " ", " ", " ", " ", "🚪"]
        ["🚪", "🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
    ]


descriptions = {
    "🌀": "Vous êtes dans une salle de murmure, pièce très sombre vous parvenez à entendre des voix vous entourent.",
    "👁️‍🗨️": "Vous êtes dans une salle de l'œil, vous ne voyer rien mais .. on vous voit ! et on vois Elias l'énorme clébard.",
    "💨": "Vous êtes dans une salle de vent, des raffales de vents viennent sur vous et laisse entendre des murmures terrifiantes.",
    "🌫️": "Vous êtes dans une salle de brume, une brume épaisse vous entoure et vous empêche de voir à plus de 2 mètres.",
}

position_joueur = [2, 2]

def afficher_carte():
    clear_screen()
    for i, ligne in enumerate(carte_murmure):
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
    return 0 <= x < len(carte_murmure) and 0 <= y < len(carte_murmure[0]) and carte_murmure[x][y] != "#"

def boucle_jeu(joueur):
    while True:
        afficher_carte()
        commande = input("Entrez une commande (z, q, s, d ou quitter) : ").lower()
        if commande == "quitter":
            print("Quitter le jeu...")
            break
        else:
            deplacer_joueur(commande)
