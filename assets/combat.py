class Fight():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)

        if self.player.is_alive():
            print("You won!")
        else:
            print("You lost!")