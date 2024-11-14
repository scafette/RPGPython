
class Item():
    def __init__(self, name, description,type):
        self.name = name
        self.description = description
        self.type = type
        


class Arme(Item):
    def __init__(self, name, description,type, attaque):
        super().__init__(name, description,type)
        self.attaque = attaque
        self.enchantement = []
    
    def est_enchant(self):
        for enchant in self.enchantement:
            if enchant == "Ronce":
                return enchant.attaquebonus
    
    def attack(self):
        return self.attaque + self.est_enchant()

    def add_enchant(self, enchant):
        self.enchantement.append(enchant)
        print(f"Vous avez ajouté {enchant.name} à votre arme")


class Enchant(Item):
    def __init__(self, name, attaquebonus):
        super().__init__(name, "Enchantement", "enchant")
        self.attaquebonus = attaquebonus



Cle = Item("Clé", "Referme le tombeau", "key")
Ronce = Enchant("Ronce", 150)
Epee = Arme("Épée", "Une épée en acier", "arme", 10)

items = [Cle,Ronce,Epee]


