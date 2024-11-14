# player.py
import random
from assets.inv import Inventaire

class Player:
    def __init__(self, name,inventaire):
        self.name = name
        self.hp = 250
        self.inventory = inventaire
        self.attaque = 5
        self.defense = 10

    def is_alive(self):
        return self.hp > 0
    def is_dead(self):
        return self.hp <= 0
    
    def attack(self):
        point_attaque = 0 
        for item in self.inventory.inventaire:
            if item.type == "arme" :
                point_attaque = item.attack()
        
        rdm = random.randint(3,5)
        if rdm == 1 :
            point_attaque += self.attaque*2
        else :
            point_attaque += self.attaque
        return point_attaque
    
    def use_potion(self):
        for item in self.inventory.inventaire:
            if item.type == "potion":
                self.hp += 250
                self.inventory.inventaire.remove(item)
                print("Vous avez utilisé une potion")
                break

    def __str__(self):
        return f"Nom: {self.name}, HP: {self.hp}, Inventaire: {self.inventory}"


class Boss:
    def __init__(self, name,hp,attaque,defense):
        self.name = name
        self.hp = hp
        self.attaque = attaque
        self.defense = defense

    def is_alive(self):
        return self.hp > 0
    def is_dead(self):
        return self.hp <= 0
    

    def __str__(self):
        return f"Nom: {self.name}, HP: {self.hp}"
    
    def attack(self):
        rdm = random.randint(1,2)
        if rdm == 1 :
            point_attaque = self.attaque*2
        else :
            point_attaque = self.attaque
        return point_attaque
    

Mephisto = Boss(
    name= "Mephisto, Le Faucher D'Ether",
    hp=500,
    attaque=25,
    defense=10,
)
Tharagon = Boss(
    name= "Tharagon",
    hp=1000,
    attaque=40,
    defense=0,
)