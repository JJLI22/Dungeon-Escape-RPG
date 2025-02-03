import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def encounter():
    enemies = ["Goblin", "Skeleton", "Dark Mage"]
    enemy = random.choice(enemies)
    print_slow(f"A wild {enemy} appears!")
    
    while True:
        action = input("Do you (A)ttack or (R)un? ").lower()
        if action == 'a':
            if random.random() > 0.3:
                print_slow(f"You defeated the {enemy}!")
                return True
            else:
                print_slow("The enemy defeated you. Game over.")
                return False
        elif action == 'r':
            if random.random() > 0.5:
                print_slow("You escaped safely!")
                return True
            else:
                print_slow(f"The {enemy} blocks your path! You must fight!")

def play_game():
    print_slow("You wake up in a dark dungeon. Your goal is to escape!")
    
    for i in range(3):
        print_slow(f"You advance to the next room ({i+1}/3)...")
        if not encounter():
            return
    
    print_slow("You found the exit and escaped the dungeon! Congratulations!")

if __name__ == "__main__":
    play_game()
