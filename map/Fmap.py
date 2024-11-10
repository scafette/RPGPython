from map import Player
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_fosse_ombres = [
    ["🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑"],
    ["🌑", " ", " ", "💀", " ", "🌫️", " ", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", " ", " ", " ", "🕸️", " ", " ", "🌫️", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", "🌫️", " ", " ", " ", "💀", "🌫️", " ", "🌫️", " ", " ", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", "🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "💀", "🌑"],
    ["🌑", " ", "💀", " ", "🕸️", " ", " ", " ", "🌑", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", "🕸️", " ", " ", " ", " ", " ", " ", " ", "🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", "🌫️", " ", " ", " ", " ", " ", " ", "🌑", " ", "💀", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", " ", "🌑", " ", " ", " ", "🌫️", " ", " ", " ", "💀", " ", " ", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", "🌑"],
    ["🌑", "🌫️", " ", " ", "🕸️", " ", "💀", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌑", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌫️", " ", " ", "🕸️", " ", " ", " ", " ", "🌫️", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🌑"],
    ["🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", "🐉", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", "🌑"],
    ["🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑"]
]


descriptions = {
    "🌑": "\033[33mMuraille de la Fosse:\033[0m Une muraille de pierre sombre, couverte de mousse et de lichen, s'étend à perte de vue.\n"
            "Des ombres dansent sur les pierres, et l'air est lourd de magie ancienne.",
    "💀": "\033[33mMorceaux De Cadavres: des bras ? non plutôt des jambes ou alors des oraganes ? personne ne pourrait reconnaitre à quoi cela peut bien représenter ...\033[0m D.\n",
    "🌫️": "\033[33mBrume Épaisse:\033[0m Une brume épaisse et sombre enveloppe le sol, rendant la visibilité difficile.\n"
            "Des murmures lointains résonnent dans la brume, et des ombres se déplacent au loin.",
    "🕸️": "\033[33mToiles d'Araignée:\033[0m D'épaisses toiles d'araignée recouvrent les murs et le sol, attention à ne pas trop rester dedans vous pourriez vous faire piquez par quelques chose de très dangereux !\n",
    "🐉": "\033[33m]Maelthar, le Tisseur d'Ombres:\033[0m Vous vous tenez devant le Roi de la Fosse , derrère lui se trouve la porte de sortie.]"
}

position_joueur = [2, 2]

def afficher_carte():
    clear_screen()
    for i, ligne in enumerate(carte_fosse_ombres):
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
    return 0 <= x < len(carte_fosse_ombres) and 0 <= y < len(carte_fosse_ombres[0]) and carte_fosse_ombres[x][y] != "#"

def boucle_jeu(joueur):
    while True:
        afficher_carte()
        commande = input("Entrez une commande (z, q, s, d ou quitter) : ").lower()
        if commande == "quitter":
            print("Quitter le jeu...")
            break
        else:
            deplacer_joueur(commande)
