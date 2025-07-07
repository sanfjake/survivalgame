import re
import json

# Display game title and instructions
def display_title():
    print("\n" + "=" * 50)
    print("Welcome to Araluen!")
    print("=" * 50)
    print("You are a young Scandrian warrior whose ship crashed onto Araluen.")
    print("Make your choices carefully to survive and escape back to your homeland.")

# Validate player name using regex
def get_player_name():
    while True:
        name = input("Enter your name to begin (letters only, 3-20 chars): ")
        if re.fullmatch(r"[A-Za-z]{3,20}", name):
            return name
        else:
            print("You may only use letters for your name (3-20 characters).")

# First Decision
def decision_one(decisions):
    print("\nYou find yourself on a beach after crash landing during a great storm.")
    print("To your left are your weapons. To your right are your supplies.")
    choice = input("Do you grab your 'weapons' or your 'supplies'? ").strip().lower()

    if choice == 'weapons':
        decisions.append("grabbed weapons")
        print("You head down the beach looking for civilization.")
        return "You come across a small fishing village."
    elif choice == 'supplies':
        decisions.append("grabbed supplies")
        print("You head down the beach looking for civilization.")
        return "You come across a small fishing village."
    else:
        print("You hesitated and lost precious time.")
        decisions.append("made no choice")
        return "Eventually, you stumble into a fishing village."

# Second Decision
def decision_two(decisions):
    print("\nIn the small fishing village, you spot a 'hostel' and 'soldiers'.")
    choice = input("Do you approach the 'soldiers' or enter the 'hostel'? ").strip().lower()

    if choice == 'soldiers':
        decisions.append('approached soldiers')
        if "grabbed weapons" in decisions:
            print("You grip your weapon tightly. The soldiers see you as a threat and attack.")
            decisions.append("fled into woods")
            return woods_path(decisions)
        else:
            print("You carry no weapons. The soldiers see you're no threat and offer assistance.")
            return "They give you directions to the nearest port town."

    elif choice == 'hostel':
        decisions.append("entered hostel")
        print("The hostel keeper offers you a warm meal and a place to rest in exchange for labor.")
        print("The hostel keeper is recently widowed and offers you a full-time post.")
        print("She also tells you of a trader who will be crossing to Scandria.")

        sub_choice = input("Do you 'stay' with the hostel keeper or 'go' with the trader? ").strip().lower()

        if sub_choice == "stay":
            decisions.append("stay")
            print("You choose to stay and fall in love with and marry the hostel keeper.")
            return "You live out your days in peace at the fishing village."
        elif sub_choice == "go":
            decisions.append("go")
            print("You sail across the sea and return to Scandrian with the trader.")
            return "You made it home to Scandria."
        else:
            decisions.append("undecided in hostel")
            return "You hesitated too long and miss both opportunities."

    else:
        decisions.append("ignored both")
        return "You wander aimlessly and eventually perish as the town drunk."

# Third Branch – if fleeing into woods
def woods_path(decisions):
    print("\nWounded and weary, you flee into the woods.")
    print("To the left you spot signs of smoke and to your right is a cave nearby.")
    choice = input("Do you 'follow smoke' or 'hide in cave'? ").strip().lower()

    if choice == "follow smoke":
        decisions.append("followed smoke")
        print("You stumble into a camp of wandering healers who treat your wounds.")
        return "With their help, you later reach a nearby port and return to Scandria."
    
    elif choice == "hide in cave":
        decisions.append("hid in cave")
        print("You survive a few days eating berries, but wolves eventually find you.")
        return "Your story ends in the cold silence of the forest."
    
    else:
        decisions.append("froze in woods")
        return "Paralyzed by indecision, you collapse from exhaustion and are never found."

# Save game data to JSON file
def save_game_data(name, decisions, outcome):
    game_data = {
        "player_name": name,
        "decisions": decisions,
        "outcome": outcome,
    }
    with open("araluen_game_data.json", "w") as f:
        json.dump(game_data, f, indent=4)

    print("\n📝 Game data saved to 'araluen_game_data.json'")

# Main Game Loop
def main():
    playing = True
    while playing:
        display_title()
        name = get_player_name()
        decisions = []

        print(f"\nWelcome, {name}. Your journey begins...\n")

        result1 = decision_one(decisions)
        print(result1)

        result2 = decision_two(decisions)
        print(result2)

        # If result2 was a string, include it; otherwise, assume it came from woods_path and was handled inside
        outcome = [result1, result2] if isinstance(result2, str) else [result1]

        save_game_data(name, decisions, outcome)

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            playing = False
            print("\nThanks for playing Survivor of Araluen. Farewell, warrior!")

# Run the game
if __name__ == "__main__":
    main()
