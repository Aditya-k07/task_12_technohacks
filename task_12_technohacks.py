import random
import sys

player_health = 100
enemy_health = 50
player_potions = 3
block_chance = 0.2

def display_status():
    print(f"Player Health: {player_health}")
    print(f"Enemy Health: {enemy_health}")
    print(f"Potions Remaining: {player_potions}")

def player_attack():
    global enemy_health
    damage = random.randint(10, 20)
    enemy_health -= damage
    print(f"You attack the enemy and deal {damage} damage!")

def enemy_attack():
    global player_health
    if random.random() < block_chance:
        print("You successfully blocked the enemy's attack!")
    else: 
        damage = random.randint(8, 15)                                          
        player_health -= damage 
        print(f"The enemy attacks and deals {damage} damage!")

def use_potion():
    global player_health, player_potions
    if player_potions > 0:
        heal = random.randint(15, 25)
        player_health = min(player_health + heal, 100)
        player_potions -= 1
        print(f"You used a potion and restored {heal} health points!")
    else:
        print("No potions left!")

def main_game():
    global player_health, enemy_health, player_potions
    print("Welcome to Simple RPG Adventure!")
    print("Defeat the enemy by attacking. Be careful not to lose all your health!")

    while player_health > 0 and enemy_health > 0:
        display_status()
        choice = input("Press 'A' to attack, 'P' to use a potion, or 'Q' to quit: ").strip().lower()

        if choice == 'a':
            player_attack()
            if enemy_health > 0:
                enemy_attack()
        elif choice == 'p':
            use_potion()
            if enemy_health > 0:
                enemy_attack()
        elif choice == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please press 'A' to attack, 'P' to use a potion, or 'Q' to quit.")

    if player_health <= 0:
        print("You have been defeated by the enemy!")
    else:
        print("You defeated the enemy! Congratulations!")

    choice = input("Play again? (Y/N): ").strip().lower()
    if choice == 'y':
        player_health = 100
        enemy_health = 50
        player_potions = 3
        main_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main_game()
