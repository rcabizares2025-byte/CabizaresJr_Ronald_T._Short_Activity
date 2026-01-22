import random

player_name = input("Enter your name: ")
health = 100
location = "route 101"

pokemon_list = ["Green ninja", "Groudon", "Machamp", "Geodude"]

def move_to_bush():
    global location
    print("You move into the bushes...")
    location = "Bushes"
    print(f"You are now at {location}.")

def chosen_pokemon():
    while True:
        choice = input("Enter the name of your chosen Pokémon: ")
        if choice in pokemon_list:
            print(f"You chose: {choice}")
            return choice
        else:
            print("This Pokémon is not in the list. Please choose again.")

def catch_charmander():
    while True:
        choice = input("Catch wild Charmander (1) or Run (2): ")
        if choice == '1':
            print("You throw a Pokéball at Charmander!")
            success = random.choice([True, False])  # Random success/failure
            if success:
                print("You successfully caught wild Charmander!")
                return True  # Caught
            else:
                print("The Pokéball broke! Charmander escaped!")
                return False  # Escaped
        elif choice == '2':
            print("You chose to run away safely.")
            return False  # Ran away
        else:
            print("Invalid choice. Please try again.")

def show_status():
    print(f"{player_name}, your health is now {health}. You are at {location}.")

# Main game flow
move_to_bush()
print("Wild Charmander appeared.")
chosen_pokemon()
caught = catch_charmander()
show_status()

# Optional: End message
if caught:
    print("Congratulations! You caught Charmander. Game over.")
else:
    print("Better luck next time. Game over.")