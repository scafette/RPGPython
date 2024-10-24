class player:
    def __init__(self, name):
        self.name = name
        self.hp = 250
        self.inventory = []

    def __str__(self):
        return f"Nom: {self.name}, HP: {self.hp}, Inventaire: {self.inventory}"
    