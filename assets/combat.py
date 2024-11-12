class Fight():

    def __init__(self, player, enemy,):
        self.player = player
        self.enemy = enemy
        
        

    def start(self):
        while self.player.is_alive() and self.enemy.is_alive():
            print("Vous attaquez!")
            self.enemy.hp -= self.player.attack()
            print(f"{self.enemy.name} a {self.enemy.hp} points de vie restants.")
            if self.enemy.is_dead():
                break
            print(f"{self.enemy.name} vous attaque!")
            self.player.hp -= self.enemy.attack()
            print(f"Il vous reste {self.player.hp} points de vie.")
        if self.player.hp > 0():
            print("Bien joué tu as vaincu le Boss de ce territoire !")
        else:
            print("Dommage , peut être dans une autre dimension tu serais repartit vainqueur bakayaro !")
            def __str__(self):
                return f"Fight between {self.player.name} and {self.enemy.name}"