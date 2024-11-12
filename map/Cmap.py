import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_cristal = [
        ["💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎"],
        ["💎", "🏛️", " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "💎", "💎", "💎", "💎", "🏛️", "💎", "💎", "💎", "💎", "💎", "💎"],
        ["💎", "🏛️", "💎", "💎", "💎"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "💎", "💎", "🏛️", "💎", "💎", "💎"],
        ["💎", "💎"," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "💎", "🏛️", "🏛️", "🏛️", "💎", "💎", "💎", "💎", "💎", "💎", "💎"],
        ["💎", "💎", "💎", "🏛️", "💎", "🏛️", "💎", "💎", "💎", "💎"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", "💎", "💎"],
        ["💎", "💎", "💎", "🏛️", "💎", "🏛️", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎"," "," "," "," "," "," ", "💎", "💎", "💎"],
        ["💎", "💎", "💎", "🏛️", "🏛️", "🏛️", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎"," "," "," ", "💎"],
        ["💎", "🏛️", "💎", "💎", "💎", "💎", "💎", "🏛️", "💎", "💎", "💎", "💎", "💎", "💎", "💎"," "," "," "," "," "," "," "," ", "💎", "💎", "💎", "💎"],
        ["💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎", "💎"," ", "💎"],
    ]


descriptionsC = {
    "💎": "Vous êtes dans une grotte de cristal, les murs brillent de mille feux.",
    "🏛️": "Vous êtes dans une salle de cristal, des colonnes de cristal entourent la pièce.",
}

position_joueur = [2, 2]
