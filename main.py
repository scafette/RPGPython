
from player import Player
from combat import Combat
from inventaire import Item
import random
import ennemies

def main_menu():
    while True:
        print("MAIN MENU")
        print("1. Create New Game")
        print("2. About")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            start_game()
        elif choice == '2':
            print("RPG crée par Gio / Elias")
        elif choice == '3':
            print("Exiting game...")
            break
        else:
            print("Invalid choice. Try again.")

def start_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"Welcome, {player.name}, to the adventure!")
    game_loop(player)

def game_loop(player):
    locations = ['clearing', 'forest', 'river', 'cave', 'boss']
    current_location = 0

    while True:
        location_desc = get_location_description(locations[current_location])
        print(location_desc)
        command = input("Enter a command (Go North, Go South, Go East, Go West, or Quit): ").lower()

        if command == "go north":
            current_location = max(0, current_location - 1)
        elif command == "go south" and current_location < len(locations) - 1:
            current_location += 1
        elif command == "quit":
            print("Returning to main menu...")
            break
        else:
            print("Invalid command.")
            continue
        
        if locations[current_location] == 'boss':
            print("You've encountered the Boss!")
            boss = Combat(player, create_ennemies('Boss', 10))
            boss.start_combat()
            if player.hp <= 0:
                print("Game Over! You have died.")
                break
            else:
                print("You defeated the boss! Congratulations!")
                break

        event = random_event()
        if event == "combat":
            enemy = create_ennemies("Goblin", random.randint(1, 3))
            print(f"A wild {enemy.name} appeared!")
            combat = Combat(player, enemy)
            combat.start_combat()
        elif event == "item":
            item = find_item()
            print(f"You found a {item.name}!")
            player.inventory.add_item(item)

def get_location_description(location):
    descriptions = {
        "clearing": "You are in a peaceful clearing.",
        "forest": "You are surrounded by dense trees in a forest.",
        "river": "A river runs through the area, flowing fast.",
        "cave": "A dark cave looms ahead.",
        "boss": "You stand before a large fortress. The Boss awaits."
    }
    return descriptions.get(location, "Unknown place.")

def random_event():
    return random.choice(["combat", "item", None])

def create_ennemies(name, level):
    return ennemies(name, level)

def find_item():
    return random.choice([Item("Potion"), Item("Attack Boost"), Item("Defense Boost")])

if __name__ == "__main__":
    main_menu()
