class Item:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

class Arme(Item):
    def __init__(self, name, description, type, attaque):
        super().__init__(name, description, type)
        self.attaque = attaque
        self.enchantement = []
    
    def est_enchant(self):
        
        bonus = 0
        for enchant in self.enchantement:
            if enchant.name == "Ronce":
                bonus += enchant.attaquebonus
        return bonus

    def attack(self):
        
        return self.attaque + self.est_enchant()

    def add_enchant(self, enchant):
        self.enchantement.append(enchant)
        print(f"Vous avez ajouté {enchant.name} à votre arme")
    
    def hasitem(self, aim_item):
        for item in self.inventaire:
            if item.name == aim_item:
                return True
        return False

class Enchant(Item):
    def __init__(self, name, attaquebonus):
        super().__init__(name, "Enchantement", "enchant")
        self.attaquebonus = attaquebonus



class Potion(Item):
    def __init__(self, name, description, type, hp):
        super().__init__(name, description, type)
        self.hp = hp
        self.utilise = False

    def use(self,player):
        if self.utilise == False :
            player.hp += self.hp
            print("Vous avez utilisé une potion")
            self.utilise = True
        else : 
            print("Potion vide")

        


potion = Potion("Potion", "Restaure 250 points de vie", "potion",250)
Cle = Item("Clé", "Referme le tombeau", "key")
Ronce = Enchant("Ronce", 150) 
Epee = Arme("Épée", "Une épée en acier", "arme", 10)

Epee.add_enchant(Ronce)

items = [Cle, Ronce, Epee, potion]

