class Ennemies:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 50 + (level * 10)
        self.attack = 10 + (level * 3)
        self.defense = 5 + (level * 2)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
