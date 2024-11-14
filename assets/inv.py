from assets.items import items

class Inventaire() :
    def __init__(self):
        self.inventaire = []

    def add(self,aim_item):
        for item in items:
            if item.name == aim_item:
                self.inventaire.append(item)
                print(f"Vous avez ramassé {item.name}")

    def getitem(self, aim_item):
        if aim_item == "Potion" :
            nb_potions = []
            for item in items:
                if item.name == aim_item:
                    nb_potions.append(item)
            for pot in nb_potions :
                if pot.utilise == False:
                    return pot
            print("Plus de potion !")
            return nb_potions[0]
        else : 
            for item in items:
                if item.name == aim_item:
                    return item

    def hasitem(self, aim_item):
        for item in self.inventaire:
            if item.name == aim_item:
                return True
        return False
    
    def __str__(self):
        return f"{[item.name for item in self.inventaire]}"