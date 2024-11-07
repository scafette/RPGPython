# main.py

from map import boucle_jeu
from player import Player
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("MENU PRINCIPAL")
        print("1. Nouvelle Partie")
        print("2. À propos")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            partie()
        elif choix == '2':
            print("RPG créé par Gio / Elias")
            print("\033[95mDescription : Monstres : Faucheurs d’Éther, Géants du Typhon, Sœurs des Tempêtes; BOSS : Sang Igris.\033[0m")
        elif choix == '3':
            clear_screen()
            print("Quitter le jeu...")
            break
        else:
            clear_screen()
            print("Choix invalide. Essayez encore.")

def partie():
    clear_screen()
    nom_joueur = input("Bonjour, jeune homme, vous devez être le chevalier envoyé d'Arcémus ! Dites-moi quel est votre nom : ")
    joueur = Player(nom_joueur)
    
    print(f"\033[95mEnchanté, {joueur.name}, mon nom à moi est Caîd, je suis le garde de ce Sanctuaire !\033[0m")

    while True:
        print("1. Dites-moi en plus sur ce Sanctuaire")
        print("2. Je veux partir à l'aventure")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            print("\033[93mLe Sanctuaire des Vents Éternels est une ancienne tour perchée au sommet d’une montagne isolée, "
                  "flottant au-dessus des Terres Brisées. Pour y parvenir, il faut traverser un chemin escarpé bordé d’étranges statues de pierre, "
                  "chacune marquée de runes anciennes dont la signification a été oubliée par le monde. Autour de la montagne, "
                  "les vents hurlent en permanence, formant une barrière invisible qui repousse quiconque tente de s'approcher sans y être invité.\033[0m")
        elif choix == '2':
            print(f"Bonne chance à vous {joueur.name}, l'aventure commence !")
            boucle_jeu(joueur)
            break
        elif choix == '3':
            clear_screen()
            print("Quitter le jeu...")
            break
        else:
            clear_screen()
            print("Choix invalide. Essayez encore.")

if __name__ == "__main__":
    menu()
