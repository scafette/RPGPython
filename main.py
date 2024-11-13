from map.mainmap import boucle_jeu
from assets.player import Player
from assets.inv import Inventaire

import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear_screen()
        print("MENU PRINCIPAL")
        print("1. Nouvelle Partie")
        print("2. À propos")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            partie()
        elif choix == '2':
            print("\nRPG créé par Gio / Elias")
            print("\033[95mDescription : Monstres,  Faucheurs d’Éther, Géants du Typhon, Sœurs des Tempêtes, Maelthar,\033[0m BOSS : Sang Igris.")
            input("Appuyez sur une touche pour continuer...")
        elif choix == '3':
            print("Quitter le jeu...")
            break
        else:
            print("Choix invalide. Essayez encore.")

def partie():
    clear_screen()
    print("\033[1mBonjour, jeune homme, vous devez être le chevalier envoyé d'Arcémus ! Si vous êtes parvenu jusqu'ici c'est que vous souhaitez libérer les ames maudites de ce sanctuaire.\033[0m")
    nom_joueur = input("\033[92mDites-moi quel est votre nom : \033[0m")


    print(f"\n\033[92mEnchanté, {nom_joueur}, je me présente je suis Caîd, le garde de ce Sanctuaire personne ne peut entrer ni sortir sans que je sois au courant ! \033[0m")
    input("Appuyez sur une touche pour continuer...")

    while True:
        clear_screen()
        print("1. Dites-moi en plus sur ce Sanctuaire")
        print("2. Je veux partir à l'aventure")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            print("\n\033[93mLe Sanctuaire des Vents Éternels est une ancienne tour perchée au sommet d’une montagne isolée, "
                  "flottant au-dessus des Terres Brisées. Pour y parvenir, il faut traverser un chemin escarpé bordé d’étranges statues de pierre, "
                  "chacune marquée de runes anciennes dont la signification a été oubliée par le monde. Autour de la montagne, "
                  "les vents hurlent en permanence, formant une barrière invisible qui repousse quiconque tente de s'approcher sans y être invité.\033[0m")
            input()
        elif choix == '2':
            print(f"\033[95mBonne chance à vous, {nom_joueur}, je vous souhaite toute la réussite et gloire afin de battre toutes les horribles créatures de ce sanctuaire ..."
                " Pitié, ma fille a été maudite et son âme est bloquée, je vous en supplie, libérez-la.\033[0m")
            print("\033[91mQue l'aventure commence !\033[0m")
            input("Appuyez sur une touche pour continuer...")
            print(f"\033[92moh ... j'allais oublié , les monstres de ce sanctuaire on une grande faiblesse qui est le pouvoir de la Ronce.\033[0m")
            print("\033[92mCe pouvoir est si je me souviens bien dans le Jardin des Ruines , trouve ce jardin et empare toi de ce pouvoir sans cela tu mourrira à coup sur !!\033[0m")
            choix = input("Appuyez sur une touche pour continuer : ")
            boucle_jeu(nom_joueur)
            break
        elif choix == '3':
            clear_screen()
            print("Quitter le jeu...")
            time.sleep(1)
            break
        else:
            print("Choix invalide. Essayez encore.")
            time.sleep(1)

if __name__ == "__main__":
    menu()
