import re
import json

# Display game title and instructions
def display_title():
    print("\n" + "="*50)
    print("Welcome to Araluen!")
    print("="*50)
    print("You are a young Scandrian warrior whose ship crashed onto Araluen. ")
    print("Make your choices carefully to survive and escape back to your home land.")

# Validate player name using regex
def get_player_name():
    while True:
        name = input("Enter your name to begin(letters only, 3-20 chars): ")
        if re.fullmatch(r"[A-Za-z]{3,20}", name):
            return name
        else:
            print("You may only use letters for your name(3-20 characters).")

# First Decision
def decision_one(decisions):
    print("\nYou find yourself on a beach after crash landing during a great storm.")
    print("To your left are your weapons. To your right are your supplies.")
    choice = input("Do you grab your 'weapons' or your 'supplies'?").strip().lower()

    if choice == 'weapons':
        