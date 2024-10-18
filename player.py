class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.xp = 0
        self.inventory = Inventory()

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 5
        print(f"{self.name} leveled up! You are now level {self.level}.")

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def use_item(self, item):
        if item.name == "Potion":
            self.hp += 50
            print(f"{self.name} used a Potion! +50 HP.")
        elif item.name == "Attack Boost":
            self.attack += 5
            print(f"{self.name} used Attack Boost! +5 Attack.")
        elif item.name == "Defense Boost":
            self.defense += 5
            print(f"{self.name} used Defense Boost! +5 Defense.")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print(item.name)
