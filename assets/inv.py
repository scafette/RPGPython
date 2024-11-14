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
        for item in items:
            if item.name == aim_item:
                return item
    def hasitem(self, aim_item):
        for item in self.inventaire:
            if item.name == aim_item:
                return True
        return False