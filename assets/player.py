# player.py
import random

class Player:
    def __init__(self, name,inventaire ):
        self.name = name
        self.hp = 250   
        self.inventory = inventaire
        hp = 250
        
        
    def is_alive(self):
        return self.hp > 0
    def is_dead(self):
        return self.hp <= 0
    
    def __str__(self):
        return f"Nom: {self.name}, HP: {self.hp}, Inventaire: {self.inventory}"


class Boss:
    def __init__(self, name,hp,attaque,defense):
        self.name = name
        self.hp = hp
        self.attaque = attaque
        self.defense = defense

    def __str__(self):
        return f"Nom: {self.name}, HP: {self.hp}"
    
    def attack(self):
        rdm = random.random(4)
        if rdm == 1 :
            point_attaque = self.attaque*2
        else :
            point_attaque = self.attaque
        return point_attaque
    

Maelthar = Boss(
    name= "Maelthar",
    hp=500,
    attaque=5,
    defense=10,
)