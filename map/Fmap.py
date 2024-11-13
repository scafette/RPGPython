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
    ["🌑", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", " ", " ", " ", "☠️🪓", " ", " ", " ", " ", " ", " ", "🕸️", " ", " ", "🌑"],
    ["🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑", "🌑"],
]


descriptionsF = {
    "🌑": "\033[33mMuraille de la Fosse:\033[0m Une muraille de pierre sombre, couverte de mousse et de lichen, s'étend à perte de vue.\n"
            "Des ombres dansent sur les pierres, et l'air est lourd de magie ancienne.",
    "💀": "\033[33mMorceaux De Cadavres: des bras ? non plutôt des jambes ou alors des oraganes ? personne ne pourrait reconnaitre à quoi cela peut bien représenter ...\033[0m D.\n",
    "🌫️": "\033[33mBrume Épaisse:\033[0m Une brume épaisse et sombre enveloppe le sol, rendant la visibilité difficile.\n"
            "Des murmures lointains résonnent dans la brume, et des ombres se déplacent au loin.",
    "🕸️": "\033[33mToiles d'Araignée:\033[0m D'épaisses toiles d'araignée recouvrent les murs et le sol, attention à ne pas trop rester dedans vous pourriez vous faire piquez par quelques chose de très dangereux !\n",
    "☠️🪓": "\033[33m]Mephisto, Le Faucher D'Ether:\033[0m Vous vous tenez devant le Roi de la Fosse , derrère lui se trouve la porte de sortie.]",
    "🔑": "Utiliser la clé pour ????????????"
}

position_joueur = [2, 2]
