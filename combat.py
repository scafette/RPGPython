import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_combat(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            print(f"{self.enemy.name} (Level {self.enemy.level}) - HP: {self.enemy.hp}")
            print(f"{self.player.name} - HP: {self.player.hp}")
            action = input("Do you want to 'attack', 'use item', or 'run'? ").lower()

            if action == 'attack':
                self.attack_phase()
            elif action == 'use item':
                self.use_item_phase()
            elif action == 'run':
                print("You fled the battle!")
                return
            else:
                print("Invalid action. Try again.")
            
            if self.enemy.hp <= 0:
                print(f"You defeated {self.enemy.name}!")
                self.player.gain_xp(10)
                return
            if self.player.hp <= 0:
                print("You were defeated!")
                return

    def attack_phase(self):
        damage = self.player.attack - self.enemy.defense
        if damage < 0: damage = 0
        self.enemy.take_damage(damage)
        print(f"You hit {self.enemy.name} for {damage} damage!")

        if self.enemy.hp > 0:
            enemy_damage = self.enemy.attack - self.player.defense
            if enemy_damage < 0: enemy_damage = 0
            self.player.take_damage(enemy_damage)
            print(f"{self.enemy.name} hits you for {enemy_damage} damage!")

    def use_item_phase(self):
        self.player.inventory.show_items()
        item_choice = input("Which item do you want to use? ")
        for item in self.player.inventory.items:
            if item_choice.lower() == item.name.lower():
                self.player.use_item(item)
                self.player.inventory.remove_item(item)
                return
        print("Invalid item choice.")
