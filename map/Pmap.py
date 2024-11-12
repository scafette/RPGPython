
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_pont_suspendu = [
        ["🌉", "🌉", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " "," ", " ", " ", " ",  " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉"," ", " ",  " ", " ", " ", " ", " ", " ", " ","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉"], "🌉",
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ",  "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉", " ", " ", " ", " ", " ", " ", " ", "🌉"," ", " ", " ", " ", " ", " ", " ", "🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉"],
        ["🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉","🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉", "🌉"],
    ]


descriptionsP = {
    "🌉": "\033[33mVous êtes sur un pont suspendu, le vide est immense en dessous de vous.\033[0m",
}

position_joueur = [2, 2]
