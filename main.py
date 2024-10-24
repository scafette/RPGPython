import random
import player

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
            print(f"\033[95mDescription : Monstres : Faucheurs d’Éther, Géants du Typhon, Sœurs des Tempêtes; BOSS : Sang Igris.\033[0m")
        elif choix == '3':
            print("Quitter le jeu...")
            break
        else:
            print("Choix invalide. Essayez encore.")

def partie():
    nom_joueur = input("Bonjour, jeune homme, vous devez être le chevalier envoyé d'Arcémus ! Dites-moi quel est votre nom : ")
    joueur = player.player(nom_joueur)
    
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
            print("Quitter le jeu...")
            break
        else:
            print("Choix invalide. Essayez encore.")

def boucle_jeu(joueur):
    position_x, position_y = 0, 0

    lieux = {
        (-1, 0): "La Fosse des Ombres",
        (2, 0): "Le Pont Suspendu",
        (2, 1): "Le Jardin des Ruines",
        (0, 2): "La Cour des Titans"
    }

    while True:
        description_lieu = lieu(lieux.get((position_x, position_y), "inconnu"))
        print(description_lieu)
        commande = input("Entrez une commande (z, q, s, d ou Quitter) : ").lower()

        if commande == 'z':  # Haut
            position_y += 1
        elif commande == 'q':  # Gauche
            position_x -= 1
        elif commande == 's':  # Bas
            position_y -= 1
        elif commande == 'd':  # Droite
            position_x += 1
        elif commande == 'quitter':
            print("Quitter le jeu...")
            break
        else:
            print("Commande invalide")

def lieu(lieu):
    descriptions = {
        "La Fosse des Ombres": (
            "Une vaste cavité souterraine au sein du sanctuaire, "
            "enveloppée dans une brume obscure. Les murs sont recouverts de racines et de mousse, "
            "et l'air est épais de magie ancienne."
        ),
        "Le Pont Suspendu": (
            "Un pont étroit et branlant suspendu au-dessus d’un abîme sans fond. "
            "Le vent souffle si fort que chaque pas semble incertain. "
            "De mystérieuses silhouettes volantes se déplacent au loin."
        ),
        "Le Jardin des Ruines": (
            "Un ancien jardin oublié, envahi par la végétation et les ruines de statues brisées. "
            "Les plantes ici sont étranges, certaines semblent presque vivantes."
        ),
        "La Cour des Titans": (
            "Une immense cour ouverte entourée de statues géantes de guerriers antiques. "
            "Certaines statues semblent presque respirer, comme si elles pouvaient s’animer à tout moment."
        ),
        "La Tour des Hurlements": (
            "La tour principale du sanctuaire, où les vents soufflent si fort qu’ils semblent hurler." 
             "Les escaliers sont en ruine, et chaque étage abrite de nouveaux dangers."
        )
    }
    return descriptions.get(lieu, "Endroit inconnu.")

if __name__ == "__main__":
    menu()
