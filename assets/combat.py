
def fight(boss,player):
    print(player)
    while player.is_alive() and boss.is_alive():
        print("Vous attaquez!")
        boss.hp -= player.attack()
        print(f"{boss.name} a {boss.hp} points de vie restants.")
        if boss.is_dead():
            break
        print(f"{boss.name} vous attaque!")
        player.hp -= boss.attack()
        print(f"Il vous reste {player.hp} points de vie.")
    if player.hp > 0:
        print("Bien joué tu as vaincu le Boss de ce territoire !")
    else:
        print("Dommage , peut être dans une autre dimension tu serais repartit vainqueur bakayaro !")
