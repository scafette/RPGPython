

def fight(boss,player):
    print(player)
    while player.is_alive() and boss.is_alive():
        print("\033[91mVous attaquez!\033[0m")
        print("\033[92mAppuyez sur une touche pour attaquer!\033[0m")
        input()
        boss.hp -= player.attack()
        print(f"\033[93m{boss.name} a {boss.hp} points de vie restants.\033[0m")
        if boss.is_dead():
            break
        print(f"\033[91m{boss.name} vous attaque!\033[0m")
        player.hp -= boss.attack()
        print(f"\033[93mIl vous reste {player.hp} points de vie.\033[0m")
    if player.hp > 0:
        print("\033[93mBien joué tu as vaincu le Boss de ce territoire !\033[0m")
        print("\033[93mIl semblerait que quelque chose de brillant soit tombé du Boss...\033[0m")
        input("\033[92mAppuyez sur une touche pour ramasser...\033[0m")
        player.inventory.add("Clé")
    else:
        print("\033[1mDommage , peut être dans une autre dimension tu serais repartit vainqueur bakayaro !\033[0m")
        exit()
